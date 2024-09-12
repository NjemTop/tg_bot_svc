from telegram import Update
from telegram.ext import ContextTypes

# Словарь для хранения данных пользователей
user_data = {}

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'order_call':
        user_id = query.from_user.id
        user_data[user_id] = {'step': 'name'}
        await query.message.reply_text('Пожалуйста, введите ваше имя:')
