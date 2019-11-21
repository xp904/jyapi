#!/usr/bin/python3
# coding: utf-8

# flask-sqlacodegen --outfile models.py  mysql+pymysql://root:root@119.3.170.97:3307/jyoa

import os

print('-开始生成Models.py--')
os.system('flask-sqlacodegen --outfile models.py  mysql+pymysql://root:root@119.3.170.97:3307/jyoa')

if os.path.exists('models.py'):
    print('---成功--')
else:
    print('--失败--')