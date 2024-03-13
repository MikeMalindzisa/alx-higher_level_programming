-- Lists * comedy shows in hbtn_0d_tvshows.
-- Sorted ASC on show title.
SELECT t_shows.`title`
  FROM `tv_shows` AS t_shows
       INNER JOIN `tv_show_genres` AS sh
       ON t_shows.`id` = sh.`show_id`
       INNER JOIN `tv_genres` AS gn
       ON gn.`id` = sh.`genre_id`
       WHERE gn.`name` = "Comedy"
 ORDER BY t_shows.`title`;

