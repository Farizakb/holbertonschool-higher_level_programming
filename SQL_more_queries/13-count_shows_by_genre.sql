-- 13-count_shows_by_genre.sql
-- Script that lists all genres with the number of shows linked
-- Results are sorted in descending order by number_of_shows
-- Only genres with at least one show are displayed

SELECT
  tv_genres.name AS genre,
  COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

