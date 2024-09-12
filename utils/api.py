import requests
from config import API_URL
from utils.logger import logger
import time

async def send_request(user_info: dict, max_retries: int = 5, timeout: int = 30) -> None:
    """
    Отправляет данные пользователя на сервер с использованием API.

    При ошибках отправки функция осуществляет повторные попытки (по умолчанию 3 раза) с паузами между ними.
    Также используется тайм-аут для каждого запроса.

    Аргументы:
        user_info (dict): Словарь с данными пользователя (имя, номер телефона).
            Пример: {'name': 'Иван', 'phone': '+1234567890'}
        max_retries (int): Максимальное количество попыток отправки запроса (по умолчанию 3).
        timeout (int): Тайм-аут запроса в секундах (по умолчанию 30 секунд).

    Возвращает:
        None
    """
    attempt = 0
    while attempt < max_retries:
        try:
            # Логируем попытку отправки данных
            logger.info(f"Попытка {attempt + 1} отправки данных для пользователя {user_info['name']}")

            # Отправляем запрос на сервер
            response = requests.post(API_URL, json={
                'name': user_info['name'],
                'phone': user_info['phone']
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
    logger.critical(f"Не удалось отправить данные для пользователя {user_info['name']} ({user_info['phone']}) после {max_retries} попыток.")
