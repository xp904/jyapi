#!/usr/bin/python3
# coding: utf-8
from flask_cors import CORS

from mainapp import app
from mainapp.views import user_api
from mainapp.views import category_api


if __name__ == '__main__':

    app.register_blueprint(user_api.user_blue, url_prefix='/user')
    app.register_blueprint(category_api.blue, url_prefix='/category')

    CORS(app)

    app.run('0.0.0.0', 8080)