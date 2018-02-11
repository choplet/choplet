import sys
from datetime import date
import sys
from _planner import storage
get_connection = lambda: storage.connect('planner.sqlite')

def action_show_menu():
	'''Отображает меню'''
	print('''

1. Добавить задачу
2. Найти задачу
3. Вывести все задачи
4. Удалить задачу
5. Показать все задачи в категории
m. Показать меню
q.  Выход
		''')

def deadlinedate(n):
    today = date.today()
    
    deadline = date(today.year,today.month, today.day+n)

    return deadline

def action_add_task():
	task = input("\nВведите задачу ")
	category = input("\nВведите категорию ")
	if not category:
		category = "Без категории"

	deadline =(int(input("\nВведите дни до дедлайна ")))

	deadline = deadlinedate(deadline) 

	with get_connection() as conn:
		added_task = storage.add(conn, task, category, deadline)
		print('Задача "{}" добавлена '.format(
			task))


def main():
	with get_connection() as conn:
		storage.initialize(conn)

	actions = {
	"1": action_add_task,
	"2": action_find_task,
	"3": action_find_all,
	"4": action_delete_task,
	"5": action_find_by_cat,
	"m": action_show_menu,
	"q": action_exit  

	}

	action_show_menu()

	while 1:
		cmd = input('Введите команду ')
		action = actions.get(cmd)

		if action:

			action()

		else:
			print('Не известная команда')



def action_find_all():
	with get_connection() as conn:
		find_all = storage.find_all(conn)
		for task in find_all:
			template = '{task[created]} - {task[task]} - {task[category]} - {task[deadline]} '
			print(template.format(task = task))


def action_find_task():
	task = input('Введите задачу ')
	with get_connection() as conn:
		print(storage.find_task(conn, task))


def action_delete_task():
	num = input('Введите задачу ')
	with get_connection() as conn:
		storage.delete_task(conn, num)
		print("задача '{}' удалена".format(num))


def action_find_by_cat():
	category = input("\n Введите категорию ")
	with get_connection() as conn:
		find_cat = storage.find_by_category(conn, category)
		for task in find_cat:
			template = '{task[id]} - {task[created]} {task[task]} {task[category]} {task[deadline]} '
			print(template.format(task = task))
		
def action_exit():
	'''Выход'''
	sys.exit(0)










		
