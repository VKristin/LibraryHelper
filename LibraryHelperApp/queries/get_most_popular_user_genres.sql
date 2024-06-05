-- Запрос на получение любимых жанров у читателей
-- Выводим несколько жанров, если на них одинаковый спрос у читателя
WITH subquery AS(
SELECT
	readers.reader_id,
	readers.reader_name,
	genre_name,
	COUNT(genres.genre_id) AS Количество
FROM 
	readers_records
JOIN 
	books USING(book_id)
JOIN
	genres USING(genre_id)
JOIN 
	readers USING(reader_id)
GROUP BY
	readers.reader_id,
	readers.reader_name,
	genre_name)

SELECT 
	reader_id,
	reader_name,
	genre_name
FROM subquery t
WHERE Количество = (SELECT 
						MAX(Количество) 
					FROM 
						subquery tt
					WHERE t.reader_id = tt.reader_id)
ORDER BY reader_id