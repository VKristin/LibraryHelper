import psycopg2 # type: ignore
from .enum_query_files import QueryFiles
from tabulate import tabulate

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
        self.file_path = ".//queries//"
    
    def send_query(self, query_file_name : str):

        '''
        Выполнение запроса

        query_file_name -- имя файла, в котором находится выполняемый запрос
        '''

        with self.connection.cursor() as cursor:
            query_file = open(f'{self.file_path}{query_file_name}')
            cursor.execute(query_file.read())
            columns = [desc[0] for desc in cursor.description]
            query_file.close()
            return tabulate(cursor.fetchall(), headers=columns, tablefmt='grid')

    def get_num_of_books(self):
        '''
        Запрос на получение количества книг
        '''
        return self.send_query(QueryFiles.num_of_books.value)
 
    def get_num_of_readers(self):
        '''
        Запрос на получение количества читателей
        '''   
        return self.send_query(QueryFiles.num_of_readers.value)
        
    
    def get_readers_num_of_books(self):
        '''
        Запрос на получение количества книг для каждого пользователя
        '''
        return self.send_query(QueryFiles.readers_num_of_books.value)
    
    def get_readers_actual_books(self):
        '''
        Запрос на количество книг, которые находятся на руках у каждого читателя
        '''
        return self.send_query(QueryFiles.readers_actual_books.value)
    
    def get_most_popular_author(self):
        '''
        Самый популярный автор
        '''
        return self.send_query(QueryFiles.most_popular_author.value)
    
    def get_most_popular_genres(self):
        '''
        Самые популярные жанры (по убыванию)
        '''
        return self.send_query(QueryFiles.most_popular_genres.value)
    
    def get_readers_last_visit(self):
        '''
        Список последних посещений читателями
        '''
        return self.send_query(QueryFiles.readers_last_visit.value)
    
    def get_most_popular_user_genres(self):
        '''
        Список пользователей и их любимых жанров
        '''
        return self.send_query(QueryFiles.most_popular_user_genres.value)