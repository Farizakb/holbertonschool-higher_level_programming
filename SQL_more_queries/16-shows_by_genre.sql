-- 16-shows_by_genre.sql
-- Script that lists all shows and their linked genres
-- If a show has no genre, display NULL
-- Results are sorted by show title and genre name

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
