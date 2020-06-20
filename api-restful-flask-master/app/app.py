from flask import Flask, jsonify
from flask_restful import Api

from database import db
from config import DATABASE_URI, PORT, DEBUG, HOST_ALLOW


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

# my migrations...
@app.before_first_request
def create_tables():
    db.create_all()
    from models.user import UserModel 
    user = UserModel('flask','flask')
    user.save_to_db()
    
# importing all the middleware for the application
from authentication import *

# importing all the routes 
from views import *



if __name__ == '__main__':
    db.init_app(app)
    app.run(host=HOST_ALLOW, port=PORT, debug=DEBUG)
