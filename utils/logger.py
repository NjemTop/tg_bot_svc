import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Логирование в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Формат логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавляем обработчик в логгер
logger.addHandler(console_handler)
