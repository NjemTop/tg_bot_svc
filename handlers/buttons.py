from telegram import Update
from telegram.ext import ContextTypes

# Словарь для хранения данных пользователей
user_data = {}

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обрабатывает нажатия на кнопки в интерфейсе бота.

    Если пользователь нажимает кнопку "Заказать звонок", начинается процесс сбора данных: 
    бот первым делом запрашивает имя пользователя.

    Аргументы:
        update (telegram.Update): Объект обновления Telegram, содержащий информацию о нажатии кнопки.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): Контекст, который содержит информацию о текущем состоянии бота.

    Возвращает:
        None
    """
    query = update.callback_query
    await query.answer()

    if query.data == 'order_call':
        user_id = query.from_user.id
        user_data[user_id] = {'step': 'name'}
        await query.message.reply_text('Пожалуйста, введите Ваше имя:')
