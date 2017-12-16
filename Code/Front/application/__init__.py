from flask import Flask
from .src import *
APP = Flask(__name__)
GAME = game.Game()
from application import views

