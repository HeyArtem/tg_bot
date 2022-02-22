from aiogram import Bot, Dispatcher, executor, types
from main import raffle_prizes
import asyncio
from my_time import current_time


# обьект бота в котрый передаю токен
bot = Bot(token='5227814949:AAFNlr52LxJr9yHxnkmOqfpIiAM30dyEiyw')

# диспетчер слушает и управлянт ботом
dp = Dispatcher(bot)

# декоратор проверяет, на какую команду будет вызываться функция
@dp.message_handler(commands='start')

# async признак асинхронной функции  (async & await)
async def start(message: types.Message):
    
    # await обычный ответ при асинхронной функции, аналог return в обычной функции
    await message.answer('Hello Bro!')
    
    
@dp.message_handler(commands='info')
async def examination(message: types.Message):
    await message.answer('Кажется работает!!!')
    

# функция должна выводить двух победителей
@dp.message_handler(commands='winners')
async def winners_list(message: types.Message):
    result = raffle_prizes()
    
    # перебираю пары
    for pair in result:
        
        # перебираю содержимое пар
        for k, v, in pair.items():
            winner_item = f'Number: {k},\nName: {v}'
            
            await message.answer(winner_item)
            

# функция выводит дату и текущее время
@dp.message_handler(commands='time')
async def time_now(message: types.Message):
    
    # вызвал функцию
    res = current_time()  
    
    for k, v, in res.items():
        total_time = f"{k.title()}: {v.title()}"
        
        await message.answer(total_time)

# функция будет отправлять время бесконечно, с указанным периодом
async def time_infinity():
    
    # бесконечная функция
    while True:
        res = current_time()  
    
        for k, v, in res.items():
            total_time = f"{k.title()}: {v.title()}"
            
            # т.к. мы не в handler бот не знает куда послать, пишу мой id, что отослать и команду, что бы не было звукового уведомления
            await bot.send_message(564764469, total_time, disable_notification=True)
        
        # засыпакм асинхронно в секундах 
        await asyncio.sleep(300)
        
        
def main():    
    # для бесконечной функции нужно создать замкнутую петлю
    loop = asyncio.get_event_loop()    
    # в петлю передаем задачу и нашу функцию
    loop.create_task(time_infinity())    
    
    # executorзапускает бота
    executor.start_polling(dp)
    
    
if __name__ == '__main__':
    main()
