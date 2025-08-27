import uuid
import os  # Unused import
import sys  # Unused import
from flask import Flask, request, jsonify  # jsonify imported but not used
from flask_smorest import abort
from db import items, stores
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

# Dead code - function defined but never used
def unused_function():
    return "This function is never called"

app = Flask(__name__)

app.config["API_TITLE"] = "Flask Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)