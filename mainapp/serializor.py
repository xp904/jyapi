#!/usr/bin/python3
# coding: utf-8

from .models import Base


def dumps(obj):
    if isinstance(obj, list):
        # 多个数据模型类对象的实例
        data = []
        for item in obj:
            data.append(convert(item))

    # 普通的模型类的实例对象
    return convert(obj)


def convert(obj):
    item_dict = obj.__dict__
    if '_sa_instance_state' in item_dict.keys():
        item_dict.pop('_sa_instance_state')

    instance = {}
    for key, value in item_dict.items():
        if isinstance(value, Base):
            instance[key] = dumps(value)
        else:
            instance[key] = value

    return instance
