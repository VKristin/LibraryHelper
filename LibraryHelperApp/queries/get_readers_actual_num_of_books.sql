-- Выводим количество книг, которые находятся на руках у каждого читателя
SELECT
    readers.reader_id, 
    reader_name,
    COUNT(books.book_id)
FROM
    readers_records
RIGHT JOIN 
    readers USING(reader_id)
JOIN 
    books USING(book_id)
WHERE
    record_return_fact_date IS null
GROUP BY 
    readers.reader_id,
    reader_name