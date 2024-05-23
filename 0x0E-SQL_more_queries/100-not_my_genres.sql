-- Lists all genres not linked to the show Dexter from hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- List all genres and left join with the subquery to find genres linked to Dexter
SELECT g.`name`
FROM `tv_genres` g
LEFT JOIN (
    SELECT `genre_id`
    FROM `tv_show_genres`
    WHERE `show_id` = (SELECT `id` FROM `tv_shows` WHERE `title` = 'Dexter')
) dg ON g.`id` = dg.`genre_id`
WHERE dg.`genre_id` IS NULL
ORDER BY g.`name`;
