def flatten(nested_list:list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            # рекурсивно вызываем flatten
            result.extend(flatten(item))
        else:
            # добавляем его в результат
            result.append(item)
    return result


if __name__ == "__main__":
    example_list = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    flattened_list = flatten(example_list)

    print("Исходный список:", example_list)
    print("Выровненный список:", flattened_list)
