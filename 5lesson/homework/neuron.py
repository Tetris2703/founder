from prettytable import PrettyTable
import math


class ActivationFunction:
    """Класс функций активации"""
    @staticmethod
    def heaviside(x):
        return 1 if x >= 0 else 0

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def tanh(x):
        return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

    @staticmethod
    def relu(x):
        return max(0, x)

    @staticmethod
    def leaky_relu(x, alpha=0.01):
        return x if x > 0 else alpha * x

    @staticmethod
    def elu(x, alpha=1.0):
        return x if x > 0 else alpha * (math.exp(x) - 1)


class Neuron(ActivationFunction):
    """Нейрон содержит, сумматор и все функции активаци"""

    # инициализируем сумматор
    def __init__(self, vec_w, vec_x):
        self.sum_ = dot(vec_w, vec_x)

    def get_info(self, k=10):
        """k - точность вывода информации"""

        # выделил в переменную для упрощения читаемости
        sum_ = self.sum_

        # Получаем результаты Y с округлением
        results = {
            "Функция Хевисайда": round(self.heaviside(sum_), k),
            "Сигмоида": round(self.sigmoid(sum_), k),
            "Гиперболический тангенс": round(self.tanh(sum_), k),
            "ReLU": round(self.relu(sum_), k),
            "Leaky ReLU": round(self.leaky_relu(sum_), k),
            "ELU": round(self.elu(sum_), k),
        }

        # Создаем таблицу
        table = PrettyTable()
        table.field_names = ["Функция", "Результат"]

        # Добавляем строки с данными
        table.add_row(["Сумматор", round(sum_, k)])

        for function_name, result in results.items():
            table.add_row([function_name, result])

        table.align["Функция"] = "l"
        table.align["Результат"] = "l"

        print(table)

# скалярное произведение
def dot(vec_w, vec_x):
    if len(vec_w) != len(vec_x):
        raise ValueError("Количество входных параметров должно совпадать с количеством весов.")

    # генераторы наше всё
    return sum(i * w for i, w in zip(vec_x, vec_w))



if __name__ == "__main__":
    # Задаем вектор весов
    vec_w = [0.5, -0.6, 0.2]    # w = [float(i) for i in input().split()]

    # Задаем входной вектор
    vec_x = [1.0, 2.0, -1.0]    # x = [float(i) for i in input().split()]

    neuron = Neuron(vec_w, vec_x)
    neuron.get_info()
