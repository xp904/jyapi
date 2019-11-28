#!/usr/bin/python3
# coding: utf-8

class DevConfig():
    ENV = 'development'
    FLASK_USE_RELOAD = True
    DEBUG = True


class ProductConfig():
    ENV = 'productment'
    FLASK_USE_RELOAD = True
    DEBUG = True
