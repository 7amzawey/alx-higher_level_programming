-- script that displays the average temperature by city orderd by temprature
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE MONTH IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
