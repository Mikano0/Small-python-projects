Billboard Hot 100 Playlist Creator (Mock Version)

Note: This is currently a mock version due to Spotify developer dashboard restrictions.
I will update this project to use the real Spotify API as soon as new app creation is available.

This project scrapes the Billboard Hot 100 chart and creates a mock Spotify playlist with the top 100 songs.
Since Spotify's developer dashboard is temporarily unavailable for new users, the project currently simulates Spotify track URIs.

Features

Scrapes song titles from Billboard Hot 100

Creates a mock Spotify playlist using unique mock URIs

Stores the playlist as a list of tuples (track name, Spotify URI)

Prints a summary of the playlist, including the total number of songs

Optional: can save the playlist to a CSV file for later use

Will be updated to integrate with Spotify API once access is restored

How it Works

Scrapes the Billboard Hot 100 chart using Requests and BeautifulSoup.

Extracts song titles

Uses a mock function to generate Spotify-like track URIs.

Builds a playlist as a list of (song, mock_uri) tuples.

Prints or saves the playlist.
