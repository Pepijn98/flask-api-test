from json import dumps

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# Api routes
from routes.Main import Main
from routes.v1.Index import Index
from routes.v1.Ship import Ship

app = Flask(__name__)
api = Api(app)

api.add_resource(Main, "/")
api.add_resource(Index, "/v1")
api.add_resource(Ship, "/v1/ship")


if __name__ == "__main__":
     app.run(port="5003")
