import unittest

def get_gcd(a, b):
    """вычислениe наибольшего общего делителя (НОД).
    Аргументы меняются местами, что позволяет избежать сортировки """
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)


def main():
    a = int(input("Введите первое положительное число: "))
    b = int(input("Введите второе положительное число: "))

    result = get_gcd(a, b)
    print(f"НОД чисел {a} и {b} равен {result}.")


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        # Тестирование различных случаев
        self.assertEqual(get_gcd(48, 18), 6)
        self.assertEqual(get_gcd(56, 98), 14)
        self.assertEqual(get_gcd(101, 10), 1)
        self.assertEqual(get_gcd(0, 5), 5)  # НОД(0, b) = b
        self.assertEqual(get_gcd(5, 0), 5)  # НОД(a, 0) = a
        self.assertEqual(get_gcd(0, 0), 0)  # НОД(0, 0) не определен, можно обрабатывать отдельно


if __name__ == "__main__":
    main()
