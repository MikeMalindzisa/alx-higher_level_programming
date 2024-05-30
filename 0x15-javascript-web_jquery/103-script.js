$(document).ready(function () {
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: languageCode },
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }
});
