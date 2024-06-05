-- Самый читаемый автор
WITH MostPopularAuthor AS(
    SELECT 
        author_name,
        COUNT(record_id) AS Количество
    FROM 
        readers_records
    JOIN 
        books USING(book_id)
    JOIN 
        authors USING(author_id)
    GROUP BY genre_name
    ORDER BY Количество DESC)

SELECT authors_name
FROM MostPopularAuthor
LIMIT 1