-- this script lists all the shows contained in hbtn_0d_tvshows
SELECT genres.name as genre,
COUNT(show_genres.show_id) as number_of_shows
FROM tv_genres genres
JOIN tv_show_genres show_genres
ON show_genres.genre_id = genres.id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
