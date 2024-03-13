-- Lists ^ genres for Dexter in hbtn_0d_tvshows.
-- Sorted ASC on genre name.
SELECT gn.`name`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS sh
       ON gn.`id` = sh.`genre_id`

       INNER JOIN `tv_shows` AS t_show
       ON t_show.`id` = sh.`show_id`
       WHERE t_show.`title` = "Dexter"
 ORDER BY gn.`name`;

