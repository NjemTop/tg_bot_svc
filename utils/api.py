import requests
from config import API_URL
from utils.logger import logger
import time

async def send_request(user_info: dict, max_retries: int = 5, timeout: int = 30) -> None:
    """Отправка данных на сервер с повторными попытками и тайм-аутом."""
    attempt = 0
    while attempt < max_retries:
        try:
            # Логируем попытку отправки данных
            logger.info(f"Попытка {attempt + 1} отправки данных для пользователя {user_info['name']}")

            # Отправляем запрос на сервер
            response = requests.post(API_URL, json={
                'name': user_info['name'],
                'phone': user_info['phone'],
                'email': user_info['email']
            }, timeout=timeout)

            # Проверка статуса ответа
            if response.status_code == 200:
                logger.info(f"Заявка от {user_info['name']} успешно отправлена!")
                return
            else:
                logger.error(f"Ошибка {response.status_code} при отправке заявки от {user_info['name']}: {response.text}")
        
        except requests.Timeout:
            logger.error(f"Тайм-аут при отправке данных для пользователя {user_info['name']}. Попытка {attempt + 1}.")

        except requests.RequestException as e:
            logger.error(f"Ошибка при отправке данных для пользователя {user_info['name']}: {e}")

        # Увеличиваем попытку
        attempt += 1

        # Ждем перед следующей попыткой
        if attempt < max_retries:
            time.sleep(30)  # Ждем 30 секунд перед повторной попыткой

    # Если после всех попыток данные не отправлены, логируем это
    logger.critical(f"Не удалось отправить данные для пользователя {user_info['name']} ({user_info['phone']}, {user_info['email']}) после {max_retries} попыток.")
