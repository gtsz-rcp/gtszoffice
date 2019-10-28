from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import sys
import os

app = Flask(__name__, root_path=os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
app.config.from_object('lib.config')
try:
    app.config.from_object('lib.config_prod')
except ImportError:
    pass

api = Api(app)

__cors_resource = {
    r'/': {
        'origins': 'http://api.gtszoffice.com'
    }
}
if app.config['ENV'] == 'development':
    __cors_resource = {
        r'/': {
            'origins': '*'
        }
    }
cors = CORS(app, resource=__cors_resource)
