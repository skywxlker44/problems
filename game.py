import random


def ask(start, end):
    while True:
        try:
            guess = int(input("Попытка: "))
            if guess > 0:
                return guess
            elif guess < start or guess > end:
                print(f"Число должно быть больше {start-1} и меньше {end + 1}")
        except ValueError:
            print("Введите корректное число")


def game(start, end):
    number = random.randint(start, end)
    for try_ in range(1, 4):
        guess = ask(start, end)
        if guess == number:
            print("Вы отгадали")
            return
        if try_ == 3:
            print("Вы проиграли")
            return
        if guess != number:
            print(f"Неправильно! Оставшееся количество попыток: {3 - try_}")
        if try_ == 2:
            if number % 2 == 0:
                print("Подсказка: число чётное")
            else:
                print("Подсказка: число нечётное")


def main():
    while True:
        try:
            start = int(input("Начало диапозона: ").strip())
            end = int(input("Конец диапозона: ").strip())
            break
        except ValueError:
            print("Введите корректное число")
    game(start, end)


main()
