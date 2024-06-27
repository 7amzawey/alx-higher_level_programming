-- my script should use the hbtn_0d_tv_shows to list all genres of the dexter
SELECT DISTINCT genres.name AS name
FROM tv_genres genres
JOIN tv_show_genres show_genres
ON show_genres.genre_id = genres.id
JOIN tv_shows shows
ON shows.id = show_genres.show_id AND shows.title = 'Dexter'
WHERE shows.id IS NULL
ORDER BY name ASC;
