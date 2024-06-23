-- this script lists all the shows contained in hbtn_0d_tvshows
select tv_shows.title, tv_show_genres.genre_id
from tv_shows
join tv_show_genres
on tv_shows.id = tv_show_genres.show_id
order by tv_shows.title, tv_show_genres.genre_id;
