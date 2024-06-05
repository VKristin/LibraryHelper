import enum

class QueryFiles(enum.Enum):
    '''
    Перечисление для хранения имён файлов
    '''
    num_of_books = "get_num_of_books.sql"
    num_of_readers = "get_num_of_readers.sql"
    readers_actual_books = "get_readers_actual_num_of_books.sql"
    readers_num_of_books = "get_readers_num_of_books.sql"
