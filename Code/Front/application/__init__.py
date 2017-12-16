from flask import Flask
from .src import *
APP = Flask(__name__)
APP.secret_key = '123456'
GAME = game.Game()
from application import views


