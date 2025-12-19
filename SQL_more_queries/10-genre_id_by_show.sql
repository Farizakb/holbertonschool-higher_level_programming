-- 10-genre_id_by_show.sql
-- Script that lists all shows with at least one linked genre
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id

SELECT
  tv_shows.title AS title,
  tv_show_genres.genre_id AS genre_id
FROM tv_shows
INNER JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;