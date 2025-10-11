import random
letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def guess_letter(used):
    while True:
        guess = input("Угадайте букву: ").strip().lower()
        if len(guess) == 1 and guess in letters:
            if guess in used:
                print("Вы уже пробовали эту букву.")
            else:
                return guess
        else:
            print("Некорректная буква")


def hangman(number_of_tries):
    words = ["слон", "ёж", "кот", "жираф"]
    word = random.choice(words)
    res = ["_" for _ in range(len(word))]
    used = set()
    while True:
        if "_" not in res:
            print(f'Вы отгадали слово "{word}"')
            return
        if number_of_tries == 0:
            print(f'Вы проиграли! Слово было "{word}"')
            return
        print(f"Допустимое количество ошибок: {number_of_tries}")
        print(" ".join(res))
        guess = guess_letter(used)
        used.add(guess)
        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    res[i] = guess
        else:
            number_of_tries -= 1


def ask():
    while True:
        try:
            number = int(input("Укажите максимальное количество ошибок: "))
            if number > 0:
                return number
            print("Укажите число больше 0")
        except ValueError:
            print("Некорректное число")


def main():
    number_of_tries = ask()
    hangman(number_of_tries)


main()
