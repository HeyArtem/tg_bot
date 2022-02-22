from aiogram import Bot, Dispatcher, types, executor
from kudamoscow import check_new_data
import aioschedule
import asyncio
from aiogram.utils.markdown import hlink

'''
Кода в указанное время (10:30, 15:30, 20:30) проверяет 
свежие события на сайте kudamoscow.ru, и 
в случае наличия свежих, отправляет их в телеграм
'''


# создаю объект бота (Art_1) в который передаю токен
bot = Bot(token='5129945325:AAEQFdCvUjoqKpDz2P5ifdjuA5w44bO22wc', parse_mode=types.ParseMode.HTML)

# управляет ботом, диспетчер это прокладка, которая слушает
dp = Dispatcher(bot) 
    

# функция вызывает функцию check_new_data()
async def test_aioschedule():   
    result_start = check_new_data()
    
    # проверка, если словарь со свежими событиями не пустой 
    if len(result_start) > 0:

        # то формируется карточка для отправики (title: href)
        for k, v, in result_start.items():
            
            # hlink-деоает гиперссылку, в title новости, закладывается ссылка
            result = f"{hlink(k, v)}"
            await bot.send_message(564764469, result, disable_notification=True)
            
    # если словарь со свежими новостями пустой, то отправляется "Нет свежих мероприятий" 
    else:
        await bot.send_message(564764469, "Нет свежих мероприятий", disable_notification=True)


async def scheduler():
    # aioschedule.every(5).seconds.do(test_aioschedule)
    aioschedule.every().day.at("10:30").do(test_aioschedule)
    aioschedule.every().day.at("15:30").do(test_aioschedule)
    aioschedule.every().day.at("20:30").do(test_aioschedule)
    aioschedule.every().day.at("11:32").do(test_aioschedule)
    aioschedule.every().day.at("11:33").do(test_aioschedule)
    await asyncio.sleep(5)    
    
    while True:
        await aioschedule.run_pending()
        

#  on_startup параметр который запускается при старте бота
async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
      
