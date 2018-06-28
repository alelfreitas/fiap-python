from flask import Flask
from flask_restful import Api, request

import json

from sklearn.externals import joblib

print("Hello world")

api = Flash("api-ml")
api = Api(app)

