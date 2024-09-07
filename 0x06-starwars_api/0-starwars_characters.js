#!/usr/bin/node

const axios = require('axios');

async function getStarWarsCharacters(movieId) {
    try {
        // Fetch film details from the Star Wars API
        const filmResponse = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const filmData = filmResponse.data;

        // Extract the character URLs from the film data
        const characters = filmData.characters;

        // Print each character's name
        for (const characterUrl of characters) {
            const characterResponse = await axios.get(characterUrl);
            const characterData = characterResponse.data;
            console.log(characterData.name);
        }
    } catch (error) {
        console.error(`Error: ${error.response ? error.response.data.detail : error.message}`);
    }
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.log("Usage: node script.js <Movie ID>");
} else {
    getStarWarsCharacters(movieId);
}
