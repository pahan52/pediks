import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

# Включаем логирование для получения информации
logging.basicConfig(level=logging.INFO)

# Вставь свой токен
API_TOKEN = '8113095548:AAFStGPjqbQeD-w6czmLT8vcCJZEWz0YO2w'

# Инициализация бота
bot = Bot(token=API_TOKEN)

# Инициализация диспетчера
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    # Создаем инлайн-клавиатуру с Web App кнопкой
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть VK", web_app=WebAppInfo(url='https://1wpwt.com/casino/play/1play_1play_mines'))]
    ])

    await message.answer('Привет, нажми на кнопку, чтобы открыть Web App', reply_markup=markup)


# Главная функция для запуска бота
async def main():
    # Регистрация хендлеров
    dp.message.register(start)

    # Запуск поллинга для обработки обновлений
    await dp.start_polling(bot)


# Запуск программы
if __name__ == "__main__":
    asyncio.run(main())
