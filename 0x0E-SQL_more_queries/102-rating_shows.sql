-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

SELECT DISTINCT ts.title
FROM tv_shows ts
LEFT JOIN (
    SELECT sg.show_id
    FROM tv_show_genres sg
    JOIN tv_genres g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
) AS comedy_shows ON ts.id = comedy_shows.show_id
WHERE comedy_shows.show_id IS NULL
ORDER BY ts.title ASC;
