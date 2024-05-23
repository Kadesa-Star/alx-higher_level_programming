-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT sg.show_id
    FROM tv_show_genres sg
    JOIN tv_genres g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY title ASC;
