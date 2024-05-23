-- Lists all shows without the genre Comedy from hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Retrieve the ID of the "Comedy" genre
SELECT id INTO @comedy_id FROM tv_genres WHERE name = 'Comedy';

-- Select all shows that are not linked to the "Comedy" genre
SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id AND sg.genre_id = @comedy_id
WHERE sg.show_id IS NULL
  AND (@comedy_id IS NULL OR s.id NOT IN (SELECT show_id FROM tv_show_genres WHERE genre_id = @comedy_id))
ORDER BY s.title ASC;
