import media


class MovieApp:
    def __init__(self, app_title, movies_list):
        self.title = app_title
        self.movies = []
        for movie in movies_list:
            self.movies.append(media.OMDBMovie(movie[0], movie[1]))

        self.template = open('html/app.html', 'r').read()

    def render(self):
        rendered_movies = ""
        for movie in self.movies:
            rendered_movies += movie.render()
        return self.template.format(title=self.title, movies=rendered_movies)

    def render_to_file(self, filename):
        render_target = open(filename, 'w')
        render_target.write(self.render())

if __name__ == "__main__":
    movies = [
        ["Anchorman: The Legend of Ron Burgundy", "NJQ4qEWm9lU"],
        ["Forrest Gump", "bLvqoHBptjg"],
        ["12 Angry Men", "fSG38tk6TpI"],
        ["Fight Club", "SUXWAEX2jlg"],
        ["The Matrix", "m8e-FF8MsqU"],
        ["Interstellar", "2LqzF5WauAw"]
    ]

    fresh_tomatoes = MovieApp("Fresh Tomatoes", movies)
    fresh_tomatoes.render_to_file("build/fresh_tomatoes.html")