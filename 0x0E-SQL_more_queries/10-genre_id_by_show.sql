-- this script lists all the shows contained in hbtn_0d_tvshows
SELECT shows.title, genres.genre_id
FROM tv_shows shows
JOIN tv_show_genres genres
ON shows.id = genres.show_id
ORDER BY shows.title, genres.genre_id;
