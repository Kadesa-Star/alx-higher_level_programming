-- Lists all shows without the genre "Comedy" in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT DISTINCT t.title
FROM tv_shows t
LEFT JOIN tv_show_genres s ON s.show_id = t.id
LEFT JOIN tv_genres g ON g.id = s.genre_id
-- The query selects distinct show titles from the tv_shows table.

WHERE t.title NOT IN (
    -- Subquery: selects titles of shows with the genre "Comedy".
    SELECT t.title
    FROM tv_shows t
    INNER JOIN tv_show_genres s ON s.show_id = t.id
    INNER JOIN tv_genres g ON g.id = s.genre_id
    WHERE g.name = 'Comedy'
)
-- Filters out shows that have the genre "Comedy" by excluding their titles 
-- using the NOT IN clause with the subquery.

ORDER BY t.title;
-- Orders the resulting shows by their title in ascending order.
