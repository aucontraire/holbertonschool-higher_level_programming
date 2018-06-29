-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT DISTINCT tv_shows.title FROM tv_shows
  LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
  WHERE tv_shows.title NOT IN
  (SELECT tv_shows.title FROM tv_shows
  LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
  WHERE tv_genres.name = "Comedy")
  ORDER BY tv_shows.title;
