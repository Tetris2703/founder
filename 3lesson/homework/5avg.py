def get_nums() -> list:
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
    upper_list = [num for num in num_list if num > avg] # выше среднего

    # join еще не использовали
    res1 = ', '.join(map(str, lower_list))
    res2 = ', '.join(map(str, upper_list))

    print(f'Значения <= {avg} - {res1}')
    print(f'Значения  > {avg} - {res2}')

if __name__ == '__main__':
    num_list = get_nums()
    print_info(num_list)
