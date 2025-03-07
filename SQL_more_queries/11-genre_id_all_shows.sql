-- script that lists all shows contained in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
select tv_shows.title, tv_show_genres.genre_id
from tv_shows
left join tv_show_genres
on tv_shows.id = tv_show_genres.show_id
order by tv_shows.title, tv_show_genres.genre_id
