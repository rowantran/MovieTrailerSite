# MovieTrailerSite
Movie trailer website for Udacity Full Stack Web Dev course

## media.py
The media module provides a OMDBMovie class that takes a movie title and YouTube video ID in the constructor.
The class will automatically retrieve other data about the movie and display it.

## Usage
### Creating your own website
To create your own webpage, you must create a MovieApp class from the app module.

The MovieApp() constructor takes one argument, which should be a list.
This list should be a two-dimensional list, where each row contains the title and the video ID.
Once the app is created, call its render_to_file function with a filename to render the HTML.

### Viewing demo/project
To view the included project using the MovieApp class, simply run `python app.py`. This will render a file to the build/ folder.