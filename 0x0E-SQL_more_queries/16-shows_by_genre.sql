-- Script that lists all shows from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column.
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
