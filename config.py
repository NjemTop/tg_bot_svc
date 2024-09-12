import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_URL = os.getenv('API_URL')
