#!/usr/bin/python3
# coding: utf-8

from redis import Redis

rd1 = Redis(host='119.3.170.97', db=1, decode_responses=True)
rd2 = Redis(host='119.3.170.97', db=2, decode_responses=True)