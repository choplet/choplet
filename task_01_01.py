from random import choice
from string import digits, ascii_letters
values = list(digits + ascii_letters)
password = []


def password_generator(n):
    random = (choice(values))

    while n:
        yield random
        random = (choice(values))
        n-=1

    def make_password(n):
        for i in password_generator(n):
                password.append(i)

        print("".join(password))

password_generator(6)
