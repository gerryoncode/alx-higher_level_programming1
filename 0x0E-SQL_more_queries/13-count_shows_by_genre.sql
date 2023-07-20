-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name AS 'genre', COUNT(genre_id) AS 'number_of_shows' FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id GROUP BY name ORDER BY number_of_shows DESC;