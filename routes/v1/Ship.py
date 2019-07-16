from urllib.request import urlopen

from bs4 import BeautifulSoup
from flask import jsonify, request, make_response
from flask_restful import Resource

from settings import Settings


class Ship(Resource):
    def get(self):
        name = request.args.get('name')
        if name == None:
            error = {"responseMessage": "Bad Request", "responseCode": 400, "data": {"message": "Missing name url param"}}
            return make_response(jsonify(error), 400)

        page = urlopen(f"{Settings.baseUrl}/{name}")
        html = BeautifulSoup(page, features="html.parser")

        images = []
        divs = html.find_all("div")
        for div in divs:
            c = div.get("class")
            if c != None and len(c) > 0:
                if c[0] == "adaptiveratioimg":
                    i = div.find("img")
                    src = f"{Settings.baseUrl}{i.get('src')}"
                    images.append(src)

        result = {"responseMessage": "OK", "responseCode": 200, "data": {"skins": images}}
        return jsonify(result)
