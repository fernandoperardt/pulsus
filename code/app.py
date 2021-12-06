from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
api = Api(app)


if __name__ == '__main__':
    from resource.device import Device
    
    api.add_resource(Device,  '/device', '/device/<deviceid>', endpoint = 'device')
    app.run(port = 5000, debug = True)