from urllib.request import urlopen

from bs4 import BeautifulSoup
from flask import jsonify, request
from flask_restful import Resource


class Ship(Resource):
    def get(self):
        page = urlopen(f"https://azurlane.koumakan.jp/{request.args.get('name')}")
        html = BeautifulSoup(page, features="html.parser")

        images = []
        divs = html.find_all("div")
        for div in divs:
            c = div.get("class")
            if c != None and len(c) > 0:
                if c[0] == "adaptiveratioimg":
                    i = div.find("img")
                    src = f"https://azurlane.koumakan.jp/{i.get('src')}"
                    images.append(src)

        result = {'responseMessage': 'OK', 'responseCode': 200, 'data': {'skins': images}}
        return jsonify(result)
