-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT g.name AS genre, COUNT(DISTINCT sg.show_id) AS num_shows, SUM(r.rate) AS total_rating
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg ON g.id = sg.genre_id
LEFT JOIN tv_show_ratings AS r ON sg.show_id = r.show_id
GROUP BY g.name
HAVING total_rating IS NOT NULL
ORDER BY total_rating DESC;
