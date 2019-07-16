from flask import jsonify
from flask_restful import Resource


class Index(Resource):
    def get(self):
        result = {"responseMessage": "OK", "responseCode": 200, "data": {"version": "0.0.1", "message": "The request was successful"}}
        return jsonify(result)
