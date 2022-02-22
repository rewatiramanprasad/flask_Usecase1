from flask import *
import json
from utility.db import connect
from employee.routes import *
from employee.error_handler import page_not_found
from flask_jwt_extended import JWTManager
from flask_jwt_extended import *

app = Flask(__name__)
app.register_blueprint(flask_blue)
app.register_error_handler(Exception,page_not_found)
app.config["SECRET_KEY"]='mHKoDFdVP8PYztn0'
jwt = JWTManager(app)


if __name__=='__main__':
    config = open("config/config.json", "r").read()
    data=json.loads(config)
    
    app.run(debug=True,host=data["host"],port=data["port"])