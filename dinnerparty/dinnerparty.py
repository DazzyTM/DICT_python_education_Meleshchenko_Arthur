import random


def lucky_process(amount_user, names, price, amount):
    """ФУНКЦИЯ УДАЧИ. В случае выбора Нет(n) процесс продолжаеться без изменений.
     При выборе ДА(y) 1 случайный человек убираеться из расчёта(lucky one)"""

    print("Do you want to use the \"Who is lucky?\" feature? Write y/n:")
    luck_input = str(input('>'))
    while luck_input != "luck":
        if luck_input == "n":
            print("No one is lucky")
            dict_1 = dict.fromkeys(names, price)
            print(dict_1)
            print('See you next time')
            return
        elif luck_input == "y":
            lucky_user = random.choice(names)
            print(lucky_user + " is the lucky one!🍀")
            new_price = amount / (amount_user - 1)
            dict_1 = dict.fromkeys(names, new_price)
            dict_1[lucky_user] = 0
            print(dict_1)
            print('Goodbye!')
            return


def get_dictionary():
    """Функция просит ввести данные после чего выводить значения ключа и делает основной расчёт"""

    names = []
    print("Enter the number of friends joining (including you)")
    amount_user = int((input(">")))
    if amount_user > 0:
        print("Enter the name of every friend (including you), each on a new line:")
    if amount_user == 0:
        print("You have no friends 💀")
        return
    for i in range(amount_user):
        names.append(str(input(">")))

    dict_1 = dict.fromkeys(names, 0)
    print(dict_1)
    print("Enter the total amount:")
    amount = float(input(">"))
    price = amount / amount_user
    dict_1 = dict.fromkeys(names, round(price, 2))
    print(dict_1)
    lucky_process(amount_user, names, price, amount)


get_dictionary()
