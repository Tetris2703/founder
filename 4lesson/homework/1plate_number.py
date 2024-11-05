"""В идеале, т.к. у номеров есть определнные символы, нужно использовать
константы созданные самостоятельно. В РФ это были бы:
letters = 'АВЕKMНОРСТУХ'
"""

from random import choice, choices
from string import ascii_uppercase, digits

def generate_plate() -> bool:
    # выбор формата
    if choice([True, False]):
        # три буквы, три цифры
        plate_letters = ''.join(choices(ascii_uppercase, k=3))
        plate_digits = ''.join(choices(digits , k=3))

    else:
        # четыре цифры, три буквы
        plate_digits = ''.join(choices(digits , k=4))
        plate_letters = ''.join(choices(ascii_uppercase, k=3))

    return f"{plate_digits} {plate_letters}"

if __name__ == "__main__":
    plate = generate_plate()
    print("Сгенерированный номерной знак:", plate)
