import string
russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def caesar(key, text):
    res = ''
    for char in text:
        if char in string.ascii_lowercase:
            index = string.ascii_lowercase.find(char)
            if index + key < len(string.ascii_lowercase):
                res += string.ascii_lowercase[index+key]
            else:
                res += string.ascii_lowercase[index+key-26]
        else:
            index = russian_letters.find(char)
            if index + key < len(russian_letters):
                res += russian_letters[index + key]
            else:
                res += russian_letters[index + key - 33]
    return res


def decode(key, text):
    res = ''
    for char in text:
        if char in string.ascii_lowercase:
            index = string.ascii_lowercase.find(char)
            res += string.ascii_lowercase[index-key]
        else:
            index = russian_letters.find(char)
            res += russian_letters[index - key]
    return res


def main():
    text = "hello"
    coded = caesar(1, text)
    decoded = decode(1, coded)
    print(coded)
    print(decoded)


main()
