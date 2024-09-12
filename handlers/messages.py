from telegram import Update
from telegram.ext import ContextTypes
from utils.validation import validate_phone, validate_email
from utils.api import send_request
from handlers.buttons import user_data

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id

    if user_id in user_data:
        step = user_data[user_id].get('step')

        # Сбор имени
        if step == 'name':
            user_data[user_id]['name'] = update.message.text
            user_data[user_id]['step'] = 'phone'
            await update.message.reply_text('Пожалуйста, введите ваш номер телефона:')

        # Сбор номера телефона
        elif step == 'phone':
            is_valid, error_message = validate_phone(update.message.text)
            if is_valid:
                user_data[user_id]['phone'] = update.message.text
                user_data[user_id]['step'] = 'email'
                await update.message.reply_text('Теперь введите ваш email:')
            else:
                await update.message.reply_text(f'Неверный формат номера.\n{error_message}')

        # Сбор email
        elif step == 'email':
            is_valid, error_message = validate_email(update.message.text)
            if is_valid:
                user_data[user_id]['email'] = update.message.text
                user_info = user_data[user_id]
                
                await update.message.reply_text(
                    f"Спасибо за вашу заявку!\n\n"
                    f"Имя: {user_info['name']}\n"
                    f"Телефон: {user_info['phone']}\n"
                    f"Email: {user_info['email']}\n\n"
                    "Мы скоро с вами свяжемся!"
                )

                # Отправляем данные на сервер
                await send_request(user_info)

                # Очищаем данные пользователя после отправки
                del user_data[user_id]
            else:
                await update.message.reply_text(f'Неверный формат email.\n{error_message}')
