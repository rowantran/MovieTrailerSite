# MovieTrailerSite
Movie trailer website for Udacity Full Stack Web Dev course

## media.py
The media module provides a OMDBMovie class that takes a movie title and YouTube video ID in the constructor.
The class will automatically retrieve other data about the movie and display it.

## Usage
To create the webpage, you must use the MovieApp class from the app module and supply it with a list of movies.
This list should be a two-dimensional array, where each row contains the title and the video ID.
Once the app is created, call its render_to_file function with a filename to render the HTML.