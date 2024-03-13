-- Lists * shows in hbtn_0d_tvshows without a genre.
-- Sorted ASC on tv_shows.title and tv_show_genres.genre_id.
SELECT sh.`title`, gn.`genre_id`
  FROM `tv_shows` AS sh
       LEFT JOIN `tv_show_genres` AS gn
       ON sh.`id` = gn.`show_id`
       WHERE gn.`genre_id` IS NULL
 ORDER BY sh.`title`, gn.`genre_id`;
