-- Получить количество читателей
SELECT COUNT(reader_id)
FROM readers
GROUP BY reader_id