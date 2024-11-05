from car_module import Car


if __name__ == "__main__":
    my_car = Car(brand="Toyota", weight=1500, power=130)

    my_car.move_forward()
    my_car.turn_right()
    my_car.turn_left()
    my_car.brake()
    my_car.honk()
