import re

def analyze(string):
    vowels = 'aeouiy'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    vowel_count = 0
    consonant_count = 0
    whitespace_count = 0
    symbols = {}

    for char in string.lower():
        symbols[char] = symbols.get(char, 0) + 1

        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char.isspace():
            whitespace_count += 1

    sorted_symbols = sorted(symbols.items(), key=lambda item: item[1], reverse=True)
    top3 = ", ".join(f"{c} - {count} occurrences" for c, count in sorted_symbols[0:3])
    word_count = len(re.findall(r"\b\w+\b", string))

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Whitespaces: {whitespace_count}")

    #Если некоторые символы втречаются одинаковое количество раз,
    # выводятся те, что стоят первее
    print(f"3 most common symbols: {top3}")

    # Под словом подразумевается последовательность,
    # которая состоит из 1 и более символов и которая
    # может включать буквы в не зависимости от регистра,
    # цифры и нижние подчёркивания
    print(f"Number of words: {word_count}")


def main():
    string = input("Enter: ")
    analyze(string)


main()
