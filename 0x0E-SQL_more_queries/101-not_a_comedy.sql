-- Lists all shows without the genre Comedy in the database 'hbtn_0d_tvshows'
-- uses a database to list all rows not linked to one row
SELECT title
FROM tv_shows
WHERE id NOT IN
(SELECT tv_shows.id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
