from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
import sqlite3
from models.post import PostModel

class Post(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="Post title required"
                        )
    parser.add_argument('desc',
                        type=str,
                        required=True,
                        help="Post description required"
                        )

    @jwt_required()
    def get(self, name):
        post = PostModel.find_by_title(name)
        if post:
            return post.json()
        return {"message": "Post not found"}, 404

    def post(self, name):
        data = Post.parser.parse_args()
        if PostModel.find_by_title(data['title']):
            return {"message": "Title with the name '{}' already exist".format(data['title'])}, 400
        post = PostModel(data['title'], data['desc'])
        try:
            post.save_to_db()
            return post.json(), 201
        except:
            return {"message": "Error in order to save post"}, 500

    def delete(self, name):
        post = PostModel.find_by_title(name)
        if post:
            post.delete_to_db()
            return {"message": "Post deleted successfuly"}, 200
        
    def put(self, name):
        data = Post.parser.parse_args()
        post = PostModel.find_by_title(name)
        if post is None:
            post = PostModel(data['title'], data['desc'])
        else:
            post.title = data['title']
            post.desc = data['desc']
        post.save_to_db()
        return post.json()


class PostList(Resource):
    @jwt_required()
    def get(self):
        return {"posts":[post.json() for post in PostModel.query.all()]}