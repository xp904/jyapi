#!/usr/bin/python3
# coding: utf-8

from unittest import TestCase
import requests

base_url = 'http://119.3.170.97:8080/user/'

class TestAppUser(TestCase):
    def test_login(self):
        url = base_url+"login/"
        data = {
            'name': 'jack',
            'pwd': '678'
        }

        resp = requests.post(url, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('status'), 0)

        print(resp.json())


