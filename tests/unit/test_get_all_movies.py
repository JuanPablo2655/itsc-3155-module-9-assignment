# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movieList = get_movie_repository()
movieList._db.__init__()


def test_get_all_movies_no_movies_inserted():
    movieList._db.__init__()
    movies = movieList.get_all_movies()
    # Assert that the movie list is 0
    assert movies == []


def test_get_all_movies():
    movies = movieList.get_all_movies()
    movieList._db.__init__()
    movieList.create_movie('Groundhog Day', 'Harold Ramis', 5)
    movieList.create_movie(
        'Captain America: The Winter Soldier', 'Anthony Russo', 4)
    assert len(movies) == 2
