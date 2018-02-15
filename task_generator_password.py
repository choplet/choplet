from random import choice
from string import digits, ascii_letters
values = list(digits + ascii_letters)


def password_generator(n):
    password = ""
    random = (choice(values))

    while n:
        password += random
        n-=1
        random = (choice(values))
    yield password

#def make_password(n):
    #for i in password_generator(n):
            #password.append(i)

    #print("".join(password))

print(next(password_generator(10)))
