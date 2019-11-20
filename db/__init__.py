#!/usr/bin/python3
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


_engine = create_engine("mysql+pymysql://root:root@119.3.170.97:3307/jyoa")
_engine.connect()

# 基于engine生成数据库会话的Session类
_Session = sessionmaker(bind=_engine)

# 创建Session类实例对
session = _Session()