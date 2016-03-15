from fresh_tomatoes import open_movies_page


class Movie:

    def __init__(self, title, art, trailer):
        self.title = title
        self.poster_image_url = art
        self.trailer_youtube_url = trailer

# create the first movie
one = Movie("Dazed and Confused",
            "http://t3.gstatic.com/images?q=tbn:ANd9GcTFwfLEg8rmU54jGuJDhxrrAKlXA93CBeInuuBHPglSGKtYG_I1",  # NOQA
            "https://www.youtube.com/watch?v=3aQuvPlcB-8")

# create the second movie
two = Movie("Hackers",
            "https://lh4.ggpht.com/TwcJGUX77mY27cVhavJ3DJhUf5lomhhWE2xrWpuuzhVQHpcqq1mGPc4-iC-yMtBuoQZ7=w300",  # NOQA
            "https://www.youtube.com/watch?v=Ql1uLyuWra8")

# make a list of movies
movies = [one, two]

# opens the movies page in a web browser
open_movies_page(movies)
