-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city,  AVG(value) as temperatures FROM temperatures GROUP By city  ORDER BY temperatures DESC;
