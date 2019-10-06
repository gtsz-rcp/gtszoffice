from flask import Flask
from flask_restful import Api

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gtszoffice:gtszoffice@localhost/gtszoffice'
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = "ZF>)?6Sj{TSI<9`zRUc>6hT>ycfXOL"

api = Api(app)
