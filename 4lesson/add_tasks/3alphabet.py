def get_word(letter):
    """возвращает слово из фонетического алфавита НАТО для заданной буквы."""
    alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie',
        'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
        'G': 'Golf', 'H': 'Hotel', 'I': 'India',
        'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    word = alphabet.get(letter.upper(), '')


    return word


def get_message(word):
    """рекурсивно преобразует слово в фонетический шифр."""
    if not word:
        return ''

    first_sym = word[0]
    rest = word[1:]

    # Преобразуем первую букву, если это буква
    if first_sym.isalpha():
        recursion_result = ' ' + get_message(rest) if rest else ''
        return get_word(first_sym) + recursion_result

    else:
        # игнорируем небуквенные символы и продолжаем с оставшейся частью слова
        return get_message(rest)


def main():
    user_input = input("Введите слово: ")
    phonetic_text = get_message(user_input)
    print(f"Фонетическое представление: {phonetic_text.strip()}")


if __name__ == "__main__":
    main()
