from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.start import start
from handlers.buttons import button_handler
from handlers.messages import message_handler

def main() -> None:
    # Создаем объект Application и передаем токен
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команду /start
    application.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик нажатий на кнопки
    application.add_handler(CallbackQueryHandler(button_handler))

    # Регистрируем обработчик сообщений (для ввода имени, телефона, email)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
