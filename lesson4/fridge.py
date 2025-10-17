from decimal import Decimal
import datetime


DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}


def is_date(string):
    try:
        datetime.datetime.strptime(string, DATE_FORMAT)
        return True
    except ValueError:
        return False


def add(title, amount, date):
    if title not in goods:
        goods[title] = []
    date = datetime.datetime.strptime(date, DATE_FORMAT).date()
    goods[title].append({"amount": amount, "expiration_date": date})


def add_by_note(string):
    split_string = [c.strip() for c in string.split(" ") if c.strip()]
    date = split_string.pop(-1)
    amount = Decimal(split_string.pop(-1))
    title = " ".join(split_string)
    if not is_date(date):
        raise ValueError("Некорректная дата")
    add(title, amount, date)


def find(string):
    keys = goods.keys()
    coolest_list_in_the_galaxy = []
    for key in keys:
        if string in key.lower():
            coolest_list_in_the_galaxy.append(key)
    return coolest_list_in_the_galaxy


def amount():
    destroyer_of_worlds = find("пельмени")
    total = 0
    for key in destroyer_of_worlds:
        for element in goods[key]:
            total += element["amount"]
    return total


def main():
    add_by_note('Пельмени Универсальные 5 2025-10-25')
    add_by_note("Пельмени 10 2025-10-25")
    print(amount())


main()
