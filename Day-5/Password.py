import random
from About import info


def PasswordGenerator():
    print(info)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # password = ''
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(
        input("How many letters would you like in your password ? "))
    nr_symbols = int(input(f"How many symbols would you like ? "))
    nr_numbers = int(input(f"How many numbers would you like ? "))

    # # Eazy Level - Order not randomised:
    # # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # for char in range(1, nr_letters + 1):
    #     randomLetter = random.choice(letters)
    #     password += randomLetter
    # for char in range(1, nr_symbols + 1):
    #     randomSymb = random.choice(symbols)
    #     password += randomSymb
    # for char in range(1, nr_numbers + 1):
    #     randomNum = random.choice(numbers)
    #     password += randomNum

    # print(password)

    # Hard Level - Order of characters randomised:
    password_list = []

    for char in range(1, nr_letters + 1):
        randomLetter = random.choice(letters)
        password_list.append(randomLetter)
    for char in range(1, nr_symbols + 1):
        randomSymb = random.choice(symbols)
        password_list.append(randomSymb)
    for char in range(1, nr_numbers + 1):
        randomNum = random.choice(numbers)
        password_list.append(randomNum)
    random.shuffle(password_list)
    password_Generator = ''
    for char in (password_list):
        password_Generator += char
    print(f"your password is : {password_Generator} ")
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


PasswordGenerator()
