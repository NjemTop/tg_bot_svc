import re

def validate_phone(phone: str) -> tuple[bool, str]:
    """
    Проверяет корректность номера телефона.

    Номер телефона должен содержать от 9 до 15 цифр и может начинаться с '+'.

    Аргументы:
        phone (str): Номер телефона, который нужно проверить.

    Возвращает:
        tuple[bool, str]: Возвращает кортеж, где:
            - Первый элемент: bool — True, если номер корректен, иначе False.
            - Второй элемент: str — Сообщение с ошибкой, если номер некорректен.
    """
    pattern = re.compile(r"^\+?\d{9,15}$")
    if pattern.match(phone):
        return True, ""
    else:
        return False, "Номер телефона должен содержать от 9 до 15 цифр и может начинаться с '+'. Пример: +79051234567"
