'''

__init__.py creates a module out of the folder containing this file.

This file is run every time the folder is accessed

Any time we referr to the module 'app' we can do it because of this init file.

'''
from flask import Flask  # import library

app = Flask(__name__)    # Create instance of flask

from app import views    # 

