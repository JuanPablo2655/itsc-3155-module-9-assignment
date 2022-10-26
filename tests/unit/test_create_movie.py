# TODO: Feature 2
from src.models.movie import Movie
from src.repositories.movie_repository import *

movies = get_movie_repository()

def test_create_movie():
    movies.__init__()
    currentMovies = movies.get_all_movies()
    movies.create_movie('Mulholland Drive', 'David Lynch', 5)
    assert len(currentMovies) == 1
    movies.create_movie('Wings', 'Larisa Shepitko', 5)
    assert len(currentMovies) == 2
