import media

TRAILER_JS = """
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
$(document).on('click', '.movie', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    console.log(sourceUrl);
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
       'frameborder': 0
     }));
});
"""


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
        return self.template.format(title=self.title, movies=rendered_movies, playTrailer=TRAILER_JS)

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
