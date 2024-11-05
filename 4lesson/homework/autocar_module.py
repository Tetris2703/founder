import turtle

class AutoCar:
    def __init__(self, make, model):
        self.make = make  # Производитель
        self.model = model  # Модель
        self.speed = 0  # Скорость в пикселях/шаг
        self.position = (0, 0)  # Позиция (x, y)
        self.is_moving = False  # Состояние автомобиля

        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.color("blue")
        self.turtle.penup()
        self.turtle.goto(self.position)

    def start(self):
        """запускает автомобиль"""
        self.is_moving = True
        print(f"{self.make} {self.model} запущен.")

    def stop(self):
        """останавливает автомобиль"""
        self.is_moving = False
        self.speed = 0
        print(f"{self.make} {self.model} остановлен")

    def accelerate(self, increment):
        """увеличивает скорость автомобиля"""
        if self.is_moving:
            self.speed += increment
            print(f"Скорость {self.make} {self.model} увеличена до {self.speed} пикселей/шаг.")
        else:
            print(f"{self.make} {self.model} не может ускориться, так как он остановлен.")

    def move(self):
        """перемещает автомобиль на новую позицию"""
        if self.is_moving:
            x, y = self.turtle.position()
            new_x = x + self.speed
            self.turtle.goto(new_x, y)
            print(f"{self.make} {self.model} перемещается на позицию {self.turtle.position()}")
        else:
            print(f"{self.make} {self.model} не может перемещаться, так как он остановлен")
