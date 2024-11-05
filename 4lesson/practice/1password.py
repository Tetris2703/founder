from random import randint


def get_symbol() -> str:
    return chr(randint(33, 126))


def get_password() -> str:
    length = randint(7, 10)  # длина пароля

    password_gen = (get_symbol() for _ in range(length)) # генератор с паролем

    password= ''.join(password_gen)
    return password


if __name__ == "__main__":
    random_password = get_password()
    print("Сгенерированный пароль:", random_password)
