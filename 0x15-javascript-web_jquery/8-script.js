$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      const movies = data.results;
      const list = $('#list_movies');
      $.each(movies, function (index, movie) {
        list.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
