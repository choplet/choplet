'''
import operator

d = {'q':1,'w':2,'e':3, 'r':4,'t':5,'y':6}

 
def test(sl):
	sl = sl.split()
	print(sl)
	#for i in sl:
		#print (i) if i in d else print('wtf')
	for i in sl:
		print ('{}:{}'.format(i, d.get(i)) if i in d else "Этого значения нет в словаре")




test('q w e a')

stack = [15, 6, 2, 9]        # stack
stack.append(999)            # push
elem = stack.pop(1)           # pop
print(elem)
print(stack)
top = stack[len(stack) - 1]  # peek
print(top)
'''
"""
def test_skobki(vir):
dlin = len(vir.split())
while dlin > 0:
"""	


'''

t = "( ) ) ( ( )"

print (test_skobki(t))

stack = []
try:
	(stack[len(stack)-1])
except:
	print("Стек пустой")

stack.append(1)
stack.append(2)
stack.append(3)


print(stack) 
'''
stack = []
def push(x):
	return stack.append(x)
#stack.append(3)
#print(stack)

def pop():
	global stack
	return stack.pop()


def clear():
	global stack
	return stack.clear()

def is_empty():
	return len(stack) == 0

#корректная проверка скобок
def skobki(s):
	for brace in s:
		if brace in "(,[":
			push(brace)
		else:
			if is_empty():
				return False
			if brace in "),]":
				pop()
	return (is_empty())
		

a = ")"
skobki(a)

# строку в список
def into_stack(sl):
	sl = sl.split()
	return sl

#print(into_stack("1 + 2 + 3"))

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

operators = ['+', '-']
inp = '5 + 2 - 3'
brack1 = ('(')
brack2 = (')')

def opn(x):
	stack1 = []
	outstring = ''
	x = into_stack(inp)
	for i in x:
		if i in nums:
			push(i)
		elif i in operators:
			stack1.append(i)
	return(stack, stack1)



print(opn(inp))


