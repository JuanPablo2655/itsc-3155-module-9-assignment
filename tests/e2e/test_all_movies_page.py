# TODO: Feature 1
from app import app

def test_get_movies_no_data(): 
    test_app = app.test_client()
    response = test_app.get('/movies/new')
    assert b'<p class="mb-3">Create a movie rating below</p>' in response.data

def test_get_movies(): 
    test_app = app.test_client()
    response = test_app.get('/movies/new')
    assert b'Groundhog day' in response.data
    assert b'Harold Ramis' in response.data
    assert b'5' in response.data