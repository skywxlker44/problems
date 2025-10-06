def analyze(string):
    properties = {
        "vowels": 0,
        "consonants": 0,
        "whitespaces": 0,
        "3_most_common_symbols": [],
        "word_number": 0
    }
    vowels = 'aeouiy'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    symbols = {}
    for char in string:
        if char not in symbols:
            symbols.update({char: 1})
        else:
            symbols[char] += 1
        if char in vowels:
            properties["vowels"] += 1
        elif char in consonants:
            properties["consonants"] += 1
        elif char in " ":
            properties["whitespaces"] += 1
    sorted_symbols = sorted(symbols.items(), key=lambda item: item[1], reverse=True)
    print(f"Vowels: {properties["vowels"]}")
    print(f"Consonants: {properties["consonants"]}")
    print(f"Whitespaces: {properties["whitespaces"]}")
    print(f"3 most common symbols: {sorted_symbols}")


def main():
    string = input("Enter: ")
    analyze(string)


main()
