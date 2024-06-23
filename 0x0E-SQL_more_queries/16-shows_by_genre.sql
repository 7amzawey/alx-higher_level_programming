-- my script should use the hbtn_0d_tv_shows to list all genres of the dexter
SELECT shows.title AS title
tv_genres.name as name
FROM tv_shows shows
JOIN tv_show_genres show_genres 
ON shows.id = show_genres.show_id
JOIN tv_genres genres
ON show_genres.genre_id = genres.id
ORDER BY title, name ASC;
