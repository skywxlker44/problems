import random

options = ["камень", "ножницы", "бумага"]
win_conditions = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}


def ask():
    while True:
        attempt = input("Вы: ").strip().lower()
        if attempt in options:
            return attempt
        else:
            print("Некорректный ход! Попробуйте ещё раз")


def game():
    score = 0
    enemy_score = 0
    print("Камень, ножницы, бумага")

    while score < 3 and enemy_score < 3:
        attempt = ask()
        response = random.choice(options)
        print(f"Противник: {response}")

        if attempt == response:
            print("Ничья")
        elif win_conditions[attempt] == response:
            score += 1
        else:
            enemy_score += 1

        if score < 3 and enemy_score < 3:
            print(f"Счёт: вы - {score}, противник - {enemy_score}")

    if score == 3:
        print(f"Вы победили! Счёт - {score}/{enemy_score}")
    else:
        print(f"Вы проиграли! Счёт - {score}/{enemy_score}")


game()
