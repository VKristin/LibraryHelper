-- Запрос для отображения информации о всех читателях
SELECT
	reader_id,
	reader_name,
	reader_telephone_number,
	streets.street_name,
	house_num.house_num_name
FROM
	readers
JOIN 
	addresses USING(address_id)
JOIN 
	streets USING(street_id)
JOIN house_num USING(house_num_id)