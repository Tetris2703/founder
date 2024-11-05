"""
Для наглядного отображения работы Автокара
воспользуемся Turtle
- визуальное отображение перещение на объекте screen
- лог в терминале

Функционал Автокара
    - старт
    - стоп
    - увеличение скорости
    - перемещение
"""

import turtle
from autocar_module import AutoCar
import time

def main():
    screen = turtle.Screen()

    # создаем беспилотный автомобиль
    my_car = AutoCar("Tesla", "Model S")

    # запускаем автомобиль
    my_car.start()

    # увеличиваем скорость и перемещаем автомобиль
    my_car.accelerate(10)

    # тест движения
    for _ in range(20):
        my_car.move()
        time.sleep(0.1)  # задержка для визуализации

    # останавливаем автомобиль
    my_car.stop()

    # закрываем окно при клике
    screen.exitonclick()

if __name__ == "__main__":
    main()
