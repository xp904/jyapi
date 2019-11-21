#!/usr/bin/python3
# coding: utf-8
from flask import Blueprint, jsonify
from flask import request

from mainapp.models import TCategory
import db

from mainapp import serializor

blue = Blueprint('category_blue', __name__)


@blue.route('/all_/', methods=('GET',))
def all_category():
    # [<TCategory>,  <>,  ]
    cate_list = db.session.query(TCategory).filter_by(parent_id=0).all()

    datas = {
        'status': 0,
        'data': {
            'cates': serializor.dumps(cate_list),
            'childs': serializor.dumps(cate_list[0].childens)
        }
    }

    return jsonify(datas)
