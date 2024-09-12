import requests
from config import API_URL
from utils.logger import logger

async def send_request(user_info: dict) -> None:
    try:
        response = requests.post(API_URL, json={
            'name': user_info['name'],
            'phone': user_info['phone'],
            'email': user_info['email']
        })

        if response.status_code == 200:
            logger.info(f"Заявка от {user_info['name']} успешно отправлена!")
        else:
            logger.error(f"Ошибка при отправке заявки от {user_info['name']}: {response.status_code}")
    except requests.RequestException as e:
        logger.error(f"Ошибка при отправке данных на сервер: {e}")
