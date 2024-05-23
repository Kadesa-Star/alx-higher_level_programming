-- Lists all genres not linked to the show Dexter
SELECT DISTINCT tg.name
FROM tv_genres tg
LEFT JOIN (
    SELECT ts.title, tsg.genre_id
    FROM tv_shows ts
    JOIN tv_show_genres tsg ON ts.id = tsg.show_id
    WHERE ts.title = 'Dexter'
) AS dexter_genres ON tg.id = dexter_genres.genre_id
WHERE dexter_genres.title IS NULL
ORDER BY tg.name ASC;
