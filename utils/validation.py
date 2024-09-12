import re

def validate_phone(phone: str) -> tuple[bool, str]:
    """Проверяет корректность номера телефона и возвращает результат с сообщением."""
    pattern = re.compile(r"^\+?\d{10,15}$")
    if pattern.match(phone):
        return True, ""
    else:
        return False, "Номер телефона должен содержать от 10 до 15 цифр и может начинаться с '+'. Пример: +79051234567"

def validate_email(email: str) -> tuple[bool, str]:
    """Проверяет корректность email и возвращает результат с сообщением."""
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if pattern.match(email):
        return True, ""
    else:
        return False, "Введите корректный email. Пример: example@mail.ru"
