import os.path as Path # нужен для построения абсолютных путей
import sqlite3
#db_name= None его можно не указывать
# коммент в первой строке функции - документация(доп блок). Создается в тройных кавычках.
def connect(db_name=None):
	"""Устанавливает соединение с БД """
	if db_name is None:
	 	db_name = ':Memory:'
	conn = sqlite3.connect(db_name)
	 #здесь будет магия

	return conn

def initialize (conn, creation_script=None):
	""" инициализирует структуру бд"""
	if creation_script is None:
		   # file путь до текущего файла dirname родительский каталог
		creation_script = Path.join(Path.dirname(__file__),'resourses',  'schema.sql')
	with conn, open(creation_script) as f:
		connection.executescript(f.read())




connect()