-- Lists * genres in hbtn_0d_tvshows with the number of
-- shows linked.
-- Does not display genres without linked shows.
-- Sorted DESC on shows count 
SELECT gn.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS tsg
       ON gn.`id` = tsg.`genre_id`
 GROUP BY gn.`name`
 ORDER BY `number_of_shows` DESC;

