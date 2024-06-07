#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make the request to get the movie details
request(filmUrl, { json: true }, (err, res, body) => {
  if (err) {
    return console.error('Error fetching movie data:', err);
  }

  if (res.statusCode !== 200) {
    return console.error('Failed to fetch movie data, status code:', res.statusCode);
  }

  // Get the list of character URLs
  const characterUrls = body.characters;

  // Fetch and print each character's name
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        return console.error('Error fetching character data:', err);
      }

      if (res.statusCode !== 200) {
        return console.error('Failed to fetch character data, status code:', res.statusCode);
      }

      console.log(body.name);
    });
  });
});
