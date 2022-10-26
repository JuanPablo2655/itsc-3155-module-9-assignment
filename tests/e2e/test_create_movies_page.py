# TODO: Feature 2
from flask import Flask
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()


def test_create_movie_form(test_app: FlaskClient):
    movie_repository._db.__init__()
    response = test_app.get('/movies/new')
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response.data
    assert b'<form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" method="POST" action="/movies">' in response.data
