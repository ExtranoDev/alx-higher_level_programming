-- prints average of temperature ordered by city
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
