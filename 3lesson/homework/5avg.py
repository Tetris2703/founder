def get_nums():
    num_list = []

    while True:
        num = input()
        if num == "":
            break

        num_list.append(int(num))

    return num_list

def print_info(num_list):
    avg = sum(num_list) / len(num_list)
    print(f'Среднее значение: {avg}')

    num_list.sort()

    lower_list = [num for num in num_list if num <= avg] # ниже среднего и равных ему
    upperer_list = [num for num in num_list if num > avg] #


if __name__ == '__main__':
    func()