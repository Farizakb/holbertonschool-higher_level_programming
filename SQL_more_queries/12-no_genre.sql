-- 12-no_genre.sql
-- Script that lists all shows without a genre linked
-- Results are sorted by tv_shows.title ascending

SELECT
  tv_shows.title AS title,
  tv_show_genres.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;