-- Lists * genres in hbtn_0d_tvshows with the number of
-- shows linked.
-- Does not display genres without linked shows.
-- Sorted DESC on shows count 
SELECT gn.`name` AS `shows_count`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS sh_gn
       ON gn.`id` = sh_gn.`genre_id`
 GROUP BY gn.`name`
 ORDER BY `shows_count` DESC;

