from flask import jsonify
from flask_restful import Resource


class Test(Resource):
    def get(self):
        result = {'version': '0.0.1'}
        return jsonify(result)
