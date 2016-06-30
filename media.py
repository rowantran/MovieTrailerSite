import json
import urllib

OMDB_API_URL_TEMPLATE = "http://www.omdbapi.com/?t={title}&plot=short&r=json"


class Trailer:
    """Displays a YouTube video when clicked."""
    
    def __init__(self, trailer_yt_id):
        self.yt_id = trailer_yt_id
        self.template = open('html/trailer.html', 'r').read()
        
    def render(self):
        return self.template.format(yt_id=self.yt_id)


class Movie:
    """Shows data of a movie and contains a Trailer."""
    
    def __init__(self, movie_title, movie_description, movie_trailer_yt_id,
                 movie_poster_url, movie_release_date):
        self.title = movie_title
        self.description = movie_description
        self.trailer = Trailer(movie_trailer_yt_id)
        self.poster_url = movie_poster_url
        self.release_date = movie_release_date
        self.template = open('html/movie.html', 'r').read()

    def render(self):
        return self.template.format(title=self.title,
                                    description=self.description,
                                    trailer=self.trailer.render(),
                                    poster_url=self.poster_url,
                                    release_date=self.release_date)


class OMDBMovie(Movie):
    """Extension of Movie that loads movie data from Open Movie Database.
    However, YouTube video ID must still be manually supplied."""

    def __init__(self, movie_title, movie_trailer_yt_id):
        # Query OMDB API for movie description, poster, and release date
        api_url = OMDB_API_URL_TEMPLATE.format(title=movie_title)
        response = urllib.urlopen(api_url)
        movie_data = json.load(response)

        Movie.__init__(self, movie_title, movie_data["Plot"],
                       movie_trailer_yt_id, movie_data["Poster"],
                       movie_data["Year"])
