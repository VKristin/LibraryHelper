-- Получение информации обо всех книгах
SELECT 
    book_id,
    book_name, 
    author_name,
    genre_name
FROM 
    books
JOIN 
    authors USING(author_id)
JOIN
    genres USING(genre_id)