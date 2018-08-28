"""
Global Flask Application Setting

set FLASK_CONFIG to 'development
 """

import os
from app import app


class Config(object):
    FLASK_ENV =  os.environ['FLASK_ENV']
    SECRET_KEY = os.environ['FLASK_SECRET']

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
