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
request(filmURL + filmNum, async function (err, res, body) {
    if (err) {
        console.error('Error fetching character data:', err);
        return;
    }

    if (res.statusCode !== 200) {
        console.error('Failed to fetch character data, status code:', res.statusCode);
        return;
    }
    const charUrls = JSON.parse(body).characters;

    for (const charURL of charUrls) {
      await new Promise(function (resolve, reject) {
        request(charURL, function (err, res, body) {
					if (err) {
            console.error('Error fetching character data:', err);
            return;
          }
        
					if (res.statusCode !== 200) {
						console.error('Failed to fetch character data, status code:', res.statusCode);
						return;
					}
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
