const link = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(link, function (resps) {
  for (let resp of resps.results) {
    const element = '<li>' + resp.title + '</li>';
    $('#list_movies').append(element);
  }
});
