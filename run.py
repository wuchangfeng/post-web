#!/usr/bin/env python
#coding=utf8

import os
from app import app
from app.database import db


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(host='0.0.0.0', port=8888, debug=True)
