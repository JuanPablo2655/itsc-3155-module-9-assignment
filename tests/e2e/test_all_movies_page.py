# TODO: Feature 1
from flask import Flask
from flask.testing import FlaskClient

def test_get_movies_no_data(test_app: FlaskClient): 
    response = test_app.get('/movies')
    assert b'<p class="mb-3">No Movies to display</p>' in response.data

def test_get_movies(test_app: FlaskClient): 
    response = test_app.get('/movies')
    assert b'Groundhog day' in response.data
    assert b'Harold Ramis' in response.data
    assert b'5' in response.data