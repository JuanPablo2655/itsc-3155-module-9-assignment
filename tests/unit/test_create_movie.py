# TODO: Feature 2
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

movies = get_movie_repository()
movies._db.__init__()

def test_create_movie():
    currentMovies = movies.get_all_movies()
    movies._db.__init__()
    get_movie_repository.create_movie('Mulholland Drive', 'David Lynch', 5)
    assert len(currentMovies) == 1
    get_movie_repository.create_movie('Wings', 'Larisa Shepitko', 5)
    assert len(currentMovies) == 2
