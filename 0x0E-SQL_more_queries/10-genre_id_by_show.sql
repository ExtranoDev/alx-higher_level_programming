-- list db items without knowing the inner workings of the database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
