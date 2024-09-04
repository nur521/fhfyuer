from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = Bot(token='7254708854:AAEop3TvQaazXTo8ZWx7djq8jBy1PMo4w-Q')
dp = Dispatcher(bot)

# Функция обработки команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Создание кнопки для перехода на веб-приложение
    keyboard = InlineKeyboardMarkup()
    web_app_url = f"https://your-web-app-url.com/?username={message.from_user.username}"
    web_button = InlineKeyboardButton(text="Open Web App", url=web_app_url)
    keyboard.add(web_button)
    
    # Отправка приветственного сообщения с кнопкой
    await message.answer("Привет! Нажми на кнопку ниже, чтобы открыть веб-приложение.", reply_markup=keyboard)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
