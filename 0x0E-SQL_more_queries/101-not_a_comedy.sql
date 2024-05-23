-- Lists all shows without the genre Comedy from hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select all shows that are not linked to the "Comedy" genre
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy'
    )
)
ORDER BY title ASC;
