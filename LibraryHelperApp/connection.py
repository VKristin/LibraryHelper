import psycopg2 # type: ignore
from dotenv import load_dotenv # type: ignore
import os

'''
Класс для подключения к БД
'''
class Connection:

    '''
    Конструктор для класса Connection
    '''
    def __init__(self):
        load_dotenv()
        self.dbname = os.getenv("DBNAME")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")

    '''
    Метод для подключения к БД
    '''
    def DbConnection(self):
        try:
            # пытаемся подключиться к базе данных
            return psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)
        except:
            # в случае сбоя подключения будет выведено сообщение в STDOUT
            print('Can`t establish connection to database')