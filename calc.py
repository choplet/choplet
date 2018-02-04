
from task_rpn import convert
from operator import (add, sub, mul, truediv)
   
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

