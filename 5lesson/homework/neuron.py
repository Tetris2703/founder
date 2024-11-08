from prettytable import PrettyTable
import math

class Neuron:
    """Класс содержит все изученные функции активации в качестве статических методов"""

    def __init__(self, weights):
        self.w = weights

    def dot(self, x):
        if len(x) != len(self.w):
            raise ValueError("Количество входных параметров должно совпадать с количеством весов.")

        # генераторы наше всё
        return sum(i * w for i, w in zip(x, self.w))

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

    def get_info(self, x, k=10):
        """k - точность вывода информации"""
        S = self.dot(x)

        # Получаем результаты
        results = {
            "Функция Хевисайда": round(self.heaviside(S), k),
            "Сигмоида": round(self.sigmoid(S), k),
            "Гиперболический тангенс": round(self.tanh(S), k),
            "ReLU": round(self.relu(S), k),
            "Leaky ReLU": round(self.leaky_relu(S), k),
            "ELU": round(self.elu(S), k),
        }

        # Создаем таблицу
        table = PrettyTable()
        table.field_names = ["Функция", "Результат"]

        # Добавляем строки с данными
        table.add_row(["Сумматор", round(S, k)])

        for function_name, result in results.items():
            table.add_row([function_name, result])

        table.align["Функция"] = "l"
        table.align["Результат"] = "l"

        print(table)


if __name__ == "__main__":
    # Задаем вектор весов
    vec_w = [0.5, -0.6, 0.2]    # w = [float(i) for i in input().split()]

    # Задаем входной вектор
    vec_x = [1.0, 2.0, -1.0]    # x = [float(i) for i in input().split()]

    neuron = Neuron(vec_w)
    neuron.get_info(vec_x)
