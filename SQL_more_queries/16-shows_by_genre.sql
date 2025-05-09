-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by tv_shows.title and tv_genres.name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC
