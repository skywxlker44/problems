from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


def generate(upper, lower, punc, dgts, length):
    parameters = [1 if arg == "yes" else 0 for arg in (upper, lower, punc, dgts)]
    res = []

    if upper == "yes":
        randint_upper = random.randint(1, length - sum(parameters[1:4]))
        random_upper = random.choices(ascii_uppercase, k=randint_upper)
        res += random_upper
        length -= randint_upper

    if lower == "yes":
        randint_lower = random.randint(1, max(1, length - sum([parameters[0]] + parameters[2:4])))
        random_lower = random.choices(ascii_lowercase, k=randint_lower)
        res += random_lower
        length -= randint_lower

    if punc == "yes":
        randint_punc = random.randint(1, max(1, length - sum(parameters[0:2] + [parameters[3]])))
        random_punc = random.choices(punctuation, k=randint_punc)
        res += random_punc
        length -= randint_punc

    if dgts == "yes":
        random_digits = random.choices(digits, k=length)
        res += random_digits

    random.shuffle(res)
    res = "".join(res)
    return res


def ask(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "no"):
            return answer
        print('Answer "yes" or "no"')


def main():
    while True:
        try:
            length = int(input("Specify the password length: "))
            if length >= 4:
                break
            print("Length must be more than 3")
        except ValueError:
            print("Enter a valid number")

    print("Do you want to have in your password (yes/no) ")
    upper = ask("Uppercase letters: ")
    lower = ask("Lowercase letters: ")
    punc = ask("Special symbols: ")
    dgts = ask("Digits: ")
    print(f"Generated password:\n{generate(upper, lower, punc, dgts, length)}")


main()

