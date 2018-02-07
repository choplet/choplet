#SQlite



'''
БАЗЫ ДАННЫХё
	- реляционные базы даныых (данные хранятся в виде таблиц)
		- таблица == сущность; названия сущностей в ед числе
		- заголовки == атрибуты
		- между сущностями существуют отношения
		- Primari key - первичный ключ - должен(желателен) в сущности
		- Foreign key - внешний ключ 
	- объектно - ориентированные (MongoDB), NOSQL
	- графовые БД


СУБД - Систему управления базами данных 
	- MySQL (MariaDB), PostgreSQL
	-ORACLE, MS SQL Server

SQlite - база данных в одном файле

SQL - структурный язык запросов
	DDL - Data definition language - язык опписания данных
	DML - Data Manipulation Language - язык манипулирования данными
		- INSERT INTO
		- UPDATE
		- DELETE
		- SELECT
'''
import sqlite3

# 1. Утановка соединнения 

db = sqlite3.connect(':memory:') # спец. слово - бд убдет создано в оперативе, потом удалена

#db = sqlite3.connect('my_db.sqlite') - нормальное создание бд

# создаем таблицу group
#  вместо целого стоит использовать беззнаковое целое
#autiincrement - автогенерация ключа
#NOT NULL колонка не может быть пустой
#DEFAULT значение по умолчанию
#IF NOT EXIST создаст если  такая таблица не существует
sql = '''
	CREATE TABLE  IF NOT EXISTS student_group (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title TEXT NOT NULL,
		active TINYINT NOT NULL DEFAULT 0
	);
'''
#2. Создаем объект курсора
cursor = db.cursor()


#3. Выполняем запрос
'''
запросы бывают 2 видов
-запрос на изменение данных и структура
	insert, update, delete, create table
	(все, кроме select)
-запрос на выборку данных

'''

result = cursor.executescript(sql)
# в первыз скобках - колонки
# во вторых значения
sql = '''
	INSERT INTO student_group(title) VALUES (?)
'''

cursor.execute(sql, ('Python',)) # запятая, чтоб сделать кортеж
cursor.execute(sql, ('PHP',))

sql = '''
	SELECT  id, title, active FROM student_group
	'''

#4. Если запрос на выобурку данных (Select)
#то выбранные данные получаем из курсора

cursor.execute(sql)
#получаем все данные в виде списка кортежей
print(cursor.fetchall())

#получаем данные построчно
print(cursor.fetchone())

#5. Закрываем соединение
db.close()


# = cursor = conn.cursor()
#with sqlite3.connect(":memory:") as conn: #через конткстный менеджер
	#cursor = conn.execute(sql) 
	#print(cursor.fetchall())


# Исключения
'''
try:
	n = int(input())
	import no_module
except ValueError:
	print('Error')
finally:
	print('Выполняется всегда')
	'''



try: 
	conn = sqlite3.connect(':memory:')
finally:
	conn.close()





