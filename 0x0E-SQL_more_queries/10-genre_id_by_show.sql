-- Lists * shows in hbtn_0d_tvshows with at least one genre.
-- Sorted ASC on tv_shows.title and tv_show_genres.genre_id.
SELECT sh.`title`, gn.`genre_id`
  FROM `tv_shows` AS sh
        INNER JOIN `tv_show_genres` AS gn
	ON sh.`id` = gn.`show_id`
 ORDER BY sh.`title`, gn.`genre_id`;

