-- this script lists all the shows contained in hbtn_0d_tvshows
select shows.title, genres.genre_id
from tv_shows shows
join tv_show_genres genres
on shows.id = genres.show_id
order by shows.title, genres.genre_id;
