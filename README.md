"""
В этом файле примеры tg bot
-просто отвечает на сообщение
-выводит двух неповторяющихся победителей из списка
-выводит дату и время по команде
-бесконечно выводит дату и время через указанный период
<<<<<<< HEAD
- проверяют   и в случае наличия свеж новостей, собирают данные и отправляют в заданное время в тг
"""
=======







устан-ем aiogramm
$ pip install -U aiogram 
from aiogram import Bot, Dispatcher, executor, types


# обьект бота в который предать токен
bot = Bot(token='свой token---------')
dp = Dispatcher(bot)


создание бота
@BotFather - (/start — если первый раз) - /newbot — написать имя для бота. - написать имя пользователя для вашего бота. Он должен заканчиваться на «bot» - получаю токен

что бы получить токен
захожу в телеграмм — нахож BotFather — копирую токен (например Use this token to access the HTTP API: 522781494----свой token---------30dyEiyw)


from aiogram import Bot, Dispatcher, executor,types

# обьект бота в который предать токен
bot = Bot(token='5227814949:A----свой token---------fpIiAM30dyEiyw')

# управляет ботом
dp = Dispatcher(bot) 

@dp.message_handler(commands='start')
async def start(message: types.Message):
	await message.answer('Hello Bro! Wots up?') 

def main(): 
	executor.start_polling(dp)

if __name__ == '__main__':
	main()


запускаю код, нахожу в телеге своего бота, /start — должен ответить Hello Bro! Wots up?



Можно запустить фун-ю в бесконечный цикл (asyncio )
$ pip install asyncio

достать свой id
tg — userinfobot — вернет мне мой id

from aiogram import Bot, Dispatcher, executor, types
import asyncio
from my_time import current_time #эту функцию размещу внизу для наглядности

# функция будет отправлять время бесконечно, с указанным периодом
async def time_infinity():
	# бесконечная функция
	while True:
		res = current_time()
 
		for k, v, in res.items():
			total_time = f"{k.title()}: {v.title()}"

			# т.к. мы не в handler бот не знает куда послать, пишу мой id, что отослать и команду, что бы не было звукового уведомления
			await bot.send_message(56---свой id---9, total_time, disable_notification=True)

		# засыпакм асинхронно в секундах 
		await asyncio.sleep(20)

def main(): 
	# для бесконечной функции нужно создать замкнутую петлю
	loop = asyncio.get_event_loop() 
	# в петлю передаем задачу и нашу функцию
	loop.create_task(time_infinity()) 

	executor.start_polling(dp)

if __name__ == '__main__':
	main()


это функ-я, которую импортирую и использую в коде выше 
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
	# current_time()

# if __name__ == '__main__':
	# main()








"""
>>>>>>> bdf617df5e632e4048ad0765b79ea80755eb7e29
