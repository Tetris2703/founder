# длина множества
def sym_amount(string):
    return len(set(string))


if __name__ == "__main__":
    string = input("Введите строку: ")

    count = sym_amount(string)
    print(f"Строка содержит {count} уникальных символов.")
