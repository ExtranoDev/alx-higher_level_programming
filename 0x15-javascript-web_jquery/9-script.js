$(document).ready(function () {
  const link = "https://fourtonfish.com/hellosalut/?lang=fr";
  $.get(
    link,
    function (resp, status) {
      if (resp.redirect) {
        $.get(resp.redirect, function (resp) {
          $("#hello").text(resp.hello);
        });
      } else {
        $("#hello").text(resp.hello);
      }
    },
    "json"
  );
});
