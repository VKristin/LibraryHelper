from .connection import Connection
from .query import Query
from .dialog_phrases import phrases

def get_connection():
    # Подключение
    connection_obj = Connection()
    return connection_obj.DbConnection()


def start_user_dialog():
    print (phrases['hello'])
    while True:
        print(phrases['help'])
        answer = input('user: ')
        if answer == 'stop':
            break
        match answer:
            case "1": get_report()



def get_report():
    connection = get_connection()
    print(connection)

    # Объект запроса
    query_obj = Query(connection)
    while True:
        print(phrases['reports'])
        answer = input('user: ')
        if answer == 'back':
            break
        match answer:
            case '1': print(f'Количество книг в библиотеке\n{query_obj.get_num_of_books()}')
            case '2': print(f'Количество читателей в библиотеке\n{query_obj.get_num_of_readers()}')
            case '3': print(f'Количество книг, которые брал каждый из читателей\n{query_obj.get_readers_num_of_books()}')
            case '4': print(f'Количество книг, которое находится у каждого читателя\n{query_obj.get_readers_actual_books()}')
            case '5': print(f'Дата последнего посещения библиотеки читателями\n{query_obj.get_readers_last_visit()}')
            case '6': print(f'Самый читаемый автор\n{query_obj.get_most_popular_author()}')
            case '7': print(f'Самые предпочитаемые читателями жанры (по убыванию)\n{query_obj.get_most_popular_genres()}')
            #case '8': print(f'Любимый жанр каждого читателя\n{query_obj.get_readers_actual_books()}')
