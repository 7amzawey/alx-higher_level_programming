-- my script should use the hbtn_0d_tv_shows to list all genres of the dexter
SELECT tv_genres.name as name
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY name ASC;
