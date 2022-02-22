from datetime import datetime
import time

'''
Функция выводит текущее время
'''

def current_time():
    # в этот словарь буду добавлять пары текущее время и дата
    data_time_list = {}
    
    # дата и в словарь
    current_date = f'{time.strftime("%d")}.{time.strftime("%m")}.{time.strftime("%Y")}'    
    data_time_list['🗓 current_date'] = current_date
    
    # время и в словарь
    current_time = f'{time.strftime("%H")}:{time.strftime("%M")}'
    data_time_list['⏰ current_time'] = current_time
        
    print(data_time_list)
    return data_time_list     
    

# def main():
#     current_time()


# if __name__ == '__main__':
#     main()
