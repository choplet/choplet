import os.path as Path #построение абсолютных путей
import sqlite3

SQL_SELECT_ALL  = '''

	SELECT
		id, created, task, category, deadline
	FROM
		planner

'''
SQL_SELECT_TASK = SQL_SELECT_ALL + "WHERE task = ?"
SQL_SELECT_CATEGORY = SQL_SELECT_ALL + "WHERE category = ?"
SQL_INSERT_TASK = '''
	INSERT INTO planner(
	task,
	category,
	deadline
	)
	VALUES(?,?,?)
'''

SQL_UPDATE_TASK = '''
	UPDATE planner SET task=?  WHERE id=?
'''

DELETE_TASK = '''
	DELETE FROM planner where task = ?
'''
def dict_factory(cursor, row):
	d = {}


	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]

	return d


def connect(db_name=None):
	'''Устанавливает соединение с бд'''
	if db_name is None:
		db_name = ":Memory:"
	conn = sqlite3.connect(db_name)
	conn.row_factory = dict_factory

	return conn


def initialize (conn, creation_script=None):
	""" инициализирует структуру бд"""
	if creation_script is None:
		   # file путь до текущего файла dirname родительский каталог
		creation_script = Path.join(Path.dirname(__file__),'resourses',  'schema.sql')
	with conn, open(creation_script) as f:
		conn.executescript(f.read())


def add(conn, task, category, deadline):
	""" Добавляет  URL адрес в БД"""

	if not  task:
		raise RuntimeError ('URL can not be empty.')          #выбрасывает исключение.
#ИЗБАВЛЯЙСЯ ОТ else - проверяй на ложь

	with conn:

		cursor = conn.execute(SQL_INSERT_TASK,(task, category, deadline)) #если не нашли - вот так

# последний вставленный идентификатор

	#return short_url


def find_all(conn):
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL)
	return cursor.fetchall()


def find_task(conn, task):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK,(task,))
	return cursor.fetchone()


def delete_task(conn, num):
	with conn:
		cursor = conn.execute(DELETE_TASK,(num,))

def find_by_category(conn, category):
	with conn:
		cursor = conn.execute(SQL_SELECT_CATEGORY,(category,))
		return cursor.fetchall()



#def initialize(conn, creation_script = None):
#	'''инициализирует структуру БД'''
#	if creation_script is None:
#		creation_script = Path.join(Path.dirname(__file__),'resourses', 'schema.sql')
#	with conn, open(creation_script) as f:
#		conn.executescript(f.read())

#def add_task()
