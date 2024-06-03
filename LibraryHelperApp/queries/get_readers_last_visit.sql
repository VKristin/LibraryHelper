-- Получить дату последнего посещения читателем библиотеки
-- Будем считать, что датап посещения = дате взятия книи
SELECT
    readers.reader_id,
    reader_name,
    MAX(record_take_date)
FROM
    readers_records
JOIN 
    readers USING(reader_id)
GROUP BY
    readers.reader_id,
    reader_name