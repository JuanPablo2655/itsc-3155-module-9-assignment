# TODO: Feature 3
from flask.testing import FlaskClient


def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search?title=Star Wars')
    assert b'Star Wars' in response.data
    assert b'George Lucas' in response.data
    assert b'4' in response.data


def test_search_movies_page_not_found(test_app: FlaskClient):
    response = test_app.get('/movies/search?title=Star Trek')
    assert b'Star Trek movie not found' in response.data
