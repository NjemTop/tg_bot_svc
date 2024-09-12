from telegram import Update
from telegram.ext import ContextTypes
from utils.validation import validate_phone
from utils.api import send_request
from handlers.buttons import user_data

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обрабатывает сообщения от пользователя, связанные со сбором данных (имя и номер телефона).
    
    Порядок действий:
    1. Если пользователь вводит имя, бот запрашивает номер телефона.
    2. Если пользователь вводит номер телефона, бот проверяет его корректность.
    3. После успешного ввода и проверки данных, бот отправляет данные на сервер и сообщает пользователю об успехе.

    Аргументы:
        update (telegram.Update): Объект обновления Telegram, содержащий информацию о сообщении пользователя.
        context (telegram.ext.ContextTypes.DEFAULT_TYPE): Контекст, который содержит информацию о текущем состоянии бота.

    Возвращает:
        None
    """
    user_id = update.message.from_user.id

    if user_id in user_data:
        step = user_data[user_id].get('step')

        # Сбор имени
        if step == 'name':
            user_data[user_id]['name'] = update.message.text
            user_data[user_id]['step'] = 'phone'
            await update.message.reply_text('Пожалуйста, введите Ваш номер телефона:')

        # Сбор номера телефона
        elif step == 'phone':
            is_valid, error_message = validate_phone(update.message.text)
            if is_valid:
                user_data[user_id]['phone'] = update.message.text
                user_info = user_data[user_id]

                await update.message.reply_text(
                    f"{user_info['name']}, благодарим за Вашу заявку!\n\n"
                    f"Мы скоро свяжемся с Вами но номеру {user_info['phone']}"
                )

                # Отправляем данные на сервер с повторными попытками
                await send_request(user_info)

                # Очищаем данные пользователя после отправки
                del user_data[user_id]
            else:
                await update.message.reply_text(f'Некорректный формат номера.\n{error_message}')
