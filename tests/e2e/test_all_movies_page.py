# TODO: Feature 1
from flask import Flask
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_get_movies_no_data(test_app: FlaskClient): 
    response = test_app.get('/movies')
    assert b'<p class="mb-3">No movies to display</p>' in response.data

def test_get_movies(test_app: FlaskClient): 
    movie_repository = get_movie_repository()
    movie_repository.create_movie('Groundhog Day', 'Harold Ramis', 5)
    response = test_app.get('/movies')
    assert b'Groundhog day' in response.data
    assert b'Harold Ramis' in response.data
    assert b'5' in response.data