from flask import Blueprint, request
from flask_restplus import Resource, Api
from manager import compose, deleteCompose

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

@api.route('/create')
class create(Resource):
    def post(self):
        compose(request.form['name'])
        return 200

@api.route('/remove')
class remove(Resource):
    def post(self):
        deleteCompose(request.form['name'])
        return 200