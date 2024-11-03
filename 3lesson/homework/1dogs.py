def get_dog_years(human_years: int) -> float:
    if human_years < 0:
        return "Возраст не может быть отрицательным."

    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 2 * 10.5 + (human_years - 2) * 4

    return dog_years


if __name__ == "__main__":

    try:
        human_years = int(input("Введите возраст в человеческих годах: "))
        dog_years = get_dog_years(human_years)
        print(f"Возраст в собачьих годах: {dog_years}")

    except ValueError:
        print("Пожалуйста, введите корректное число.")
