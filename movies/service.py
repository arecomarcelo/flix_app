from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()
    
    def create_movies(self, title, release_date, gender, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            gender=gender,
            actors=actors,
            resume=resume,
        )

        return self.movie_repository.create_movie(movie)
    
    