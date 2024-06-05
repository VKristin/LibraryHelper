-- Получить дату последнего посещения читателем библиотеки
-- Будем считать, что дата посещения = дате взятия или возвращения книги
SELECT
    readers.reader_id,
    reader_name,
   	GREATEST(MAX(record_take_date), MAX(record_return_fact_date)) as last_visit_date
FROM
    readers_records
JOIN 
    readers USING(reader_id)
GROUP BY
    readers.reader_id,
    reader_name