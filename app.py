import media
import os

# JavaScript code to be injected into app.html, must be inserted through
# Python to avoid collision with format().
# On clicking the close button of the trailer, stop the YouTube video.
# On clicking a movie, insert the YouTube video into the modal.
TRAILER_JS = open('js/trailer.js', 'r').read()


class MovieApp:
    """Collects a list of movies and displays them in a website."""
    def __init__(self, app_title, movies_list):
        self.title = app_title
        self.movies = []

        # Create list of OMDBMovie classes using provided movie list.
        for movie in movies_list:
            self.movies.append(media.OMDBMovie(movie[0], movie[1]))

        self.template = open('html/app.html', 'r').read()

    def render(self):
        rendered_movies = ""
        for movie in self.movies:
            rendered_movies += movie.render()
        return self.template.format(title=self.title, movies=rendered_movies,
                                    playTrailer=TRAILER_JS)

    def render_to_file(self, filename):
        # Check if build directory exists
        if not os.path.exists("build"):
            os.makedirs("build")
        render_target = open(os.path.join("build", filename), 'w')
        render_target.write(self.render())

if __name__ == "__main__":
    # Only gets executed if app.py is being run as a standalone file.
    # Create the demo application and render to build/fresh_tomatoes.html.
    movies = [
        ["Anchorman: The Legend of Ron Burgundy", "NJQ4qEWm9lU"],
        ["Forrest Gump", "bLvqoHBptjg"],
        ["12 Angry Men", "fSG38tk6TpI"],
        ["Fight Club", "SUXWAEX2jlg"],
        ["The Matrix", "m8e-FF8MsqU"],
        ["Interstellar", "2LqzF5WauAw"]
    ]

    fresh_tomatoes = MovieApp("Fresh Tomatoes", movies)
    fresh_tomatoes.render_to_file("fresh_tomatoes.html")
