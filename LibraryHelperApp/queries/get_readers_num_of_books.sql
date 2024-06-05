-- Выводим количество книг, которые брал каждый читатель
SELECT
    readers.reader_id, 
    reader_name,
    COUNT(books.book_id)
FROM
    readers_records
JOIN 
    readers USING(reader_id)
JOIN 
    books USING(book_id)
GROUP BY 
    readers.reader_id,
    reader_name
ORDER BY readers.reader_id