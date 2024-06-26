-- Получить популярные жанры по убыванию
WITH GenresPopular AS(
    SELECT 
        genre_name,
        COUNT(record_id) AS Количество
    FROM 
        readers_records
    JOIN 
        books USING(book_id)
    RIGHT JOIN 
        genres USING(genre_id)
    GROUP BY genre_name
    ORDER BY Количество DESC)

SELECT genre_name
FROM GenresPopular