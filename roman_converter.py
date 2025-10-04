def roman_to_int(roman):
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    res = 0
    prev = 0
    for char in roman[::-1]:
        value = roman_numerals[char]
        if value < prev:
            res -= value
        else:
            res += value
        prev = value
    return res


def int_to_roman(number):
    if number < 1 or number > 5000:
        raise Exception("Number must be between 1 and 5000")
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    res = ''
    for value, numeral in values:
        while number >= value:
            res += numeral
            number -= value
    return res


def main():
    print(roman_to_int("XCIX"))
    print(int_to_roman(2023))


main()

