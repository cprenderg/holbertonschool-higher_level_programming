fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movieList = document.querySelector('#list_movies');

    data.results.forEach(movie => {
      const newItem = document.createElement('li');
      newItem.textContent = movie.title;
      movieList.appendChild(newItem);
    });
  });