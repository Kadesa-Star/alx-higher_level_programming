-- Lists all genres not linked to the show Dexter from hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- First, find the id of the show "Dexter"
SELECT id INTO @dexter_id FROM tv_shows WHERE title = 'Dexter';

-- List all genres that are not linked to "Dexter"
SELECT name 
FROM tv_genres 
WHERE id NOT IN (
    SELECT genre_id 
    FROM tv_show_genres 
    WHERE show_id = @dexter_id
)
ORDER BY name;
