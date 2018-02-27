
from operator import (add, sub, mul, truediv)


def convert(expr):
    nums = ('0123456789')
    opers = {'+':1,
             '-':1,
             '*':2,
             '/':2,
             '^':3,
             '(':0,
             }
    lst = list(''.join(expr.split()))

    stnum = []
    stoper  = []
    for i in lst:
        if i in nums:
            stnum.append(i)
        elif i == "(":
            stoper.append(i)

        elif i == ")":
            pop = stoper.pop()
            while pop != "(":
                stnum.append(pop)
                pop = stoper.pop()

        elif i in opers:
            if len(stoper) == 0:
                stoper.append(i)
            elif opers[i] > opers[stoper[len(stoper) - 1]]:
                stoper.append(i)
            else:
                stnum.append(stoper.pop())
                stoper.append(i)
    while stoper:
        stnum.append(stoper.pop())
    return ' '.join(stnum)


def calc(expr):
    OPERATORS = {'+': add, '-': sub, '*': mul, '/': truediv, '^':pow}
    stack = [0]
    for token in convert(expr).split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return (stack.pop())

if __name__ == '__main__':
	print(calc(input()))
