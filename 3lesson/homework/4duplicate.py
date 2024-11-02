"""
Можно было сделать через set, но нам требуется сохранить порядок
"""

def unique_words():
    words = []

    while True:
        word = input()

        if word == "":
            break

        if word not in words:
            words.append(word)

    for word in words:
        print(word)

if __name__ == '__main__':
    unique_words()

