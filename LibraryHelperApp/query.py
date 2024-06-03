import psycopg2 # type: ignore
from enum_query_files import QueryFiles

class Query:

    '''
    Класс Запрос
    '''
    def __init__(self, connection: psycopg2.connect):
        '''
        Конструктор для класса Запрос

        connection -- подключение к БД
        '''
        self.connection = connection
        self.file_path = "queries//"
    
    def send_query(self, query_file_name):

        '''
        Выполнение запроса

        query_file_name -- имя файла, в котором находится выполняемый запрос
        '''

        with self.connection.cursor() as cursor:
            query_file = open(self.file_path + query_file_name)
            cursor.execute(query_file.read())
            query_file.close()
            return cursor.fetchall()

    def get_num_of_books(self):
        '''
        Запрос на получение количества книг
        '''
        return self.send_query(QueryFiles.num_of_books)
 
    def get_num_of_readers(self):
        '''
        Запрос на получение количества читателей
        '''   
        return self.send_query(QueryFiles.num_of_readers)
        
    
    def get_readers_num_of_books(self):
        '''
        Запрос на получение количества книг для каждого пользователя
        '''
        return self.send_query(QueryFiles.readers_num_of_books)
    
    def get_readers_actual_books(self):
        '''
        Запрос на количество книг, которые находятся на руках у каждого читателя
        '''
        return self.send_query(QueryFiles.readers_actual_books)