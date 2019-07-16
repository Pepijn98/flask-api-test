from flask import redirect
from flask_restful import Resource


class Main(Resource):
    def get(self):
        return redirect("/v1", code=302)
