-- Lists * shows and genres linked to show from hbtn_0d_tvshows.
-- Sorted ASC on show title and genre name.
SELECT t_show.`title`, gn.`name`
  FROM `tv_shows` AS t_show
         LEFT JOIN `tv_show_genres` AS sh
	        ON t_show.`id` = sh.`show_id`
       LEFT JOIN `tv_genres` AS gn
              ON sh.`genre_id` = gn.`id`
	       ORDER BY t_show.`title`, gn.`name`;

