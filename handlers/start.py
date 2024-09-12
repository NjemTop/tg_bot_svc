from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обрабатывает команду /start.

    Отправляет пользователю приветственное сообщение с двумя кнопками:
    1. "Сделать заказ" — ведет на сайт с услугами.
    2. "Заказать звонок" — начинает процесс сбора данных для обратного звонка.

    Аргументы:
        update (telegram.Update): Объект обновления Telegram, содержащий информацию о сообщении пользователя.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): Контекст, который содержит информацию о текущем состоянии бота.

    Возвращает:
        None
    """
    keyboard = [
        [
            InlineKeyboardButton("Сделать заказ", url="https://www.nkscleaning.ru/#uslugi"),
            InlineKeyboardButton("Заказать звонок", callback_data='order_call')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите действие:', reply_markup=reply_markup)
