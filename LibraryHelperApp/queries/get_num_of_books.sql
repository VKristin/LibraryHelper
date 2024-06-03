-- Получить количество книг
SELECT COUNT(book_id)
FROM books
GROUP BY book_id