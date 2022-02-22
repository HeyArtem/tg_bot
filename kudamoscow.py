from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import os
import json




'''
На этой странице две функции, которые проверяют  
и в случае наличия свеж новостей, собирают данные.


функция соберет карточки с событиями на первой странице  kudamoscow.ru
запишет и х в json {title: url}  all_event_dict.json
'''

def get_data():
    # юзер агент подменяет юзер агента))
    ua = UserAgent()
    url = 'https://kudamoscow.ru/event/all/month/'
    
    headers = {
        'user-agent': ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    # запрос к сайту
    response = requests.get(url=url, headers=headers)
    
    # проверяю и в случае отсутствия создаю директорию
    if not os.path.exists('kudamoscow_data'):
        os.mkdir('kudamoscow_data')
    
    # сохраняю главную страницу
    with open(file='kudamoscow_data/index.html', mode='w') as file:
        file.write(response.text)
    
    # читаю-сохраняю главную страницу в перем src
    with open(file='kudamoscow_data/index.html') as file:
        src = file.read()        
    # создаю объект BeautifulSoup
    soup = BeautifulSoup(markup=src, features='lxml')    
    
    # блок с карточками
    content = soup.find('section', id='content')
    
    # нахожу каждую карточку по div event.
    all_events = content.find_all('div', class_='event')
    
    # print(len(all_events))
    
    # в этот словарь буду записывать пары {title: url}
    all_events_dict = {}
    
    # в цикле из каждой карточки достаю title, url, description
    for event in all_events:
        event_title = event.find('a', class_='eventname').get('title')
        event_url = event.find('a', class_='eventname').get('href')
        event_desctiption = event.find('p', {'itemprop': "description"}).text        
        
        # разсплитовал все в список (каждый элемент) по умолчанию по пробелу (или (my_st.split(","))-по запятой)
        event_desctiption_list = event_desctiption.split()        
        
        # склеил список строк по пробелу
        event_desctiption = ' '.join(event_desctiption_list)        

        # вытащил цену на событие
        event_price = int(event.find('span', {'itemprop': "price"}).text)
        
        if event_price == 0:
            event_price = 'Besplatno'
        
        # print(f"{event_title}\n{event_url}\n{event_desctiption}\n{event_price}\n{'#' * 20}")
        
        # записываю в словарь {title: url}
        all_events_dict[event_title] = event_url
        
    
    # записываю в json словарь all_events_dict 
    with open(file='kudamoscow_data/all_event_dict.json', mode='w') as file:
        json.dump(all_events_dict, file, indent=4, ensure_ascii=False)
        
        
'''
Функция принимает словарь  {title: url}
 опять парсит title с сайта kudamoscow
 и сравнивает с наличием этого title в предудщем словаре.
 В случает отсутствия, записывает title в новый словарь new_events
 и в старый.
 Записывает оба словаря в json файлы
 new_events.json (только новые события), 
 all_event_dict.json (старые + новые события)
 '''
def check_new_data(path='kudamoscow_data/all_event_dict.json'):
    
    # читаю сохраненый json фаил в переменную src
    with open(file=path) as file:
        src = json.load(file)
        
    ua = UserAgent()
    url = 'https://kudamoscow.ru/event/all/month/'
    
    headers = {
        'user-agent': ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    response = requests.get(url=url, headers=headers)    
    soup = BeautifulSoup(markup=response.text, features='lxml')    
    
    content = soup.find('section', id='content')    
    all_events = content.find_all('div', class_='event')   
    
    # в словарь буду сохранять собранную с первой страницы инфу
    new_events = {}
    
    for event in all_events:
        
        # получаю title
        event_title = event.find('a', class_='eventname').get('title')
        
        # если новый title содержится в словаре от предыдущей функции, цикл if переходит к сравнению следющ. title
        if event_title in src:
            continue
        
        # если title не ссодержится в предыдущем словаре
        else:
            #  получаю url этого события
            event_url = event.find('a', class_='eventname').get('href')
            
            # записываю новое событие в new_events (мой новый словарь)
            new_events[event_title] = event_url
            
            # и записываю  также событие в словарь с которым сравнивал (в старый словарь)
            src[event_title] = event_url
            
    # записываю новый словарь в json (в этом словаре только {title: url} новых мероприятий])
    with open(file='kudamoscow_data/new_events.json', mode='w') as file:
        json.dump(new_events, file, indent=4, ensure_ascii=False)
    
    # записываю (перезаписываю) старый  словарь, добавив в него карточки с новыми событиями
    with open(file='kudamoscow_data/all_event_dict.json', mode='w') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)
    
    # функция возвращает словарь с новыми событиями
    return new_events
            
    
def main():
    # get_data()
    check_new_data()
    
    
if __name__ == '__main__':
    main()
