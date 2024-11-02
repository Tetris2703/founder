def get_nums():
    numbers = []

    while True:
        num = input("Введите целое число (для завершения введите 0): ")
        try:
            num = int(num)
            if num == 0:
                break
            numbers.append(num)

        except ValueError:
            print("Пожалуйста, введите целое число.")

    numbers.sort()
    return numbers


def print_nums(nums):
    print("Введенные числа в порядке возрастания:")
    for num in nums:
        print(num)


if __name__ == "__main__":
    sorted_numbers = get_nums()
    print_nums(sorted_numbers)
