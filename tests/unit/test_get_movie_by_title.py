# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()
movie_repository.create_movie('Star Wars', 'George Lucas', 4)


def test_get_movie_by_title():
    movie = movie_repository.get_movie_by_title('Star Wars')

    assert type(movie) == Movie
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 4


def test_get_movie_by_title_not_found():
    movie = movie_repository.get_movie_by_title('Star Trek')

    assert movie is None
