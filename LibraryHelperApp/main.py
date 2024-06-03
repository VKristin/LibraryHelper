import connection
import query

# Подключение
connection_obj = connection.Connection()
connection = connection_obj.DbConnection()
print(connection)

# Объект запроса
query_obj = query.Query(connection)
print (query_obj.get_num_of_books())