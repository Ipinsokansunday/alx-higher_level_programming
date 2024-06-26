#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

// Function to count movies where "Wedge Antilles" is present
function countMoviesWithWedgeAntilles(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter(film => 
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(moviesWithWedgeAntilles.length);
  });
}

countMoviesWithWedgeAntilles(apiUrl);
