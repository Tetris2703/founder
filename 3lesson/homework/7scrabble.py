def get_score(word: str) -> int:
    points = {
        'AEILNORSTU': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }

    word = word.upper()
    score = 0

    for letter in word:
        for key, value in points.items():
            if letter in key:
                score += value
                break  # как только нашли соответствие, разрываем внутренний цикл

    return score


def main():
    word = input("Введите слово: ")
    score = get_score(word)
    print(f"Количество очков за слово '{word}': {score}")


if __name__ == '__main__':
    main()
