import psycopg2 # type: ignore
from dotenv import load_dotenv # type: ignore
import os

class Connection:
    '''
    Класс для подключения к БД
    '''
    def __init__(self):
        '''
        Конструктор для класса Connection
        '''
        load_dotenv()
        self.dbname = os.getenv("DBNAME")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")

    def DbConnection(self):
        '''
        Метод для подключения к БД
        '''
        try:
            # пытаемся подключиться к базе данных
            return psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)
        except:
            # в случае сбоя подключения будет выведено сообщение в STDOUT
            print('Can`t establish connection to database')