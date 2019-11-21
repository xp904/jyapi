#!/usr/bin/python3
# coding: utf-8

from unittest import TestCase
import requests

base_url = 'http://localhost:8080/user/'

class TestAppUser(TestCase):
    def test_login(self):
        url = base_url+"login/"
        data = {
            'name': '13629189683',
            'pwd': '189683'
        }

        resp = requests.post(url, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('status'), 0)

        print(resp.json())


    def test_send_code(self):
        url = base_url+"send_code/?phone=13629189683"
        resp = requests.get(url)
        print(resp)

    def test_regist(self):
        url = base_url+"regist/"
        data = {
            'phone': '13629189683',
            'code': '33458'
        }

        resp = requests.post(url, json=data)
        print(resp.json())


