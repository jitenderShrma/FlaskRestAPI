from flask import Flask, request, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister
from resources.posts import Post, PostList
from db import db

app = Flask(__name__)
app.secret_key = 'supersecret'
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)
posts = [
    {
        "title":"post1",
        "desc": "description of the post",
        "is_publish": True
    }
]


api.add_resource(Post, '/posts/<string:name>')
api.add_resource(PostList, '/posts/all')
api.add_resource(UserRegister, '/register')

if __name__== '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)