import re
from urllib.request import urlopen

from bs4 import BeautifulSoup
from flask import jsonify, make_response, request
from flask_restful import Resource

from settings import Settings


def get_skins(html: BeautifulSoup):
    images = []
    divs = html.find_all("div", {"class": "adaptiveratioimg"})
    for div in divs:
        img = div.find("img")
        images.append(f"{Settings.baseUrl}{img.get('src')}")
    return images


def get_names(html: BeautifulSoup):
    div = html.find("div", {"style": "border-style:solid; border-width:1px 1px 0px 1px; border-color:#a2a9b1; width:100%; background-color:#eaecf0; text-align:center; font-weight:bold"})
    return {
        "en": re.sub(r" \(.+\)", "", div.text),
        "cn": html.find("span", {"lang": "zh"}).text,
        "jp": html.find("span", {"lang": "ja"}).text,
        "kr": html.find("span", {"lang": "ko"}).text
    }


class Ship(Resource):
    def get(self):
        name = request.args.get('name')
        if name == None:
            error = {"responseMessage": "Bad Request", "responseCode": 400, "data": {
                "message": "Missing name url param"}}
            return make_response(jsonify(error), 400)

        page = urlopen(f"{Settings.baseUrl}/{name}")
        html = BeautifulSoup(page, features="html.parser")

        images = get_skins(html)
        names = get_names(html)

        result = {
            "responseMessage": "OK",
            "responseCode": 200,
            "data": {
                "skins": images,
                "names": names
            }
        }
        return jsonify(result)
