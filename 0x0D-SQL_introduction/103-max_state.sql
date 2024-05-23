-- script that displays the average temperature by city orderd by temprature
SELECT state, MAX(value) as max_temp;
FROM temperatures
