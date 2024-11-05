class Car:
    def __init__(self, brand, weight, power):
        self.brand = brand
        self.weight = weight
        self.power = power

    def move_forward(self):
        print(f"{self.brand} движется вперед.")

    def turn_right(self):
        print(f"{self.brand} поворачивает направо.")

    def turn_left(self):
        print(f"{self.brand} поворачивает налево.")

    def brake(self):
        print(f"{self.brand}  тормозит.")

    def honk(self):
        print(f"{self.brand} сигналит.")
