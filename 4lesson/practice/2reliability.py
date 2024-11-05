"""Для универсальности кода не стал делать возврат строки"""

def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)  # наличие заглавных букв
    has_lower = any(c.islower() for c in password)  # наличие строчных букв
    has_digit = any(c.isdigit() for c in password)  # наличие цифр

    return has_upper and has_lower and has_digit


if __name__ == "__main__":
    user_password = input("Введите пароль для проверки: ")

    if is_strong_password(user_password):
        print("Пароль надежный.")
    else:
        print("Пароль ненадежный.")
