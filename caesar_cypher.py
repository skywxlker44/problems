from string import ascii_lowercase
russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def encode(key, text):
    res = ''
    for char in text:
        if char in ascii_lowercase:
            index = ascii_lowercase.find(char)
            if index + key < len(ascii_lowercase):
                res += ascii_lowercase[index+key]
            else:
                res += ascii_lowercase[index+key-len(ascii_lowercase)]
        elif char in russian_letters:
            index = russian_letters.find(char)
            if index + key < len(russian_letters):
                res += russian_letters[index + key]
            else:
                res += russian_letters[index + key - len(russian_letters)]
        else:
            res += char
    return res


def decode(key, text):
    res = ''
    for char in text:
        if char in ascii_lowercase:
            index = ascii_lowercase.find(char)
            res += ascii_lowercase[index-key]
        elif char in russian_letters:
            index = russian_letters.find(char)
            res += russian_letters[index - key]
        else:
            res += char
    return res


def main():
    text = "hello"
    coded = encode(1, text)
    decoded = decode(1, coded)
    print(coded)
    print(decoded)


main()
