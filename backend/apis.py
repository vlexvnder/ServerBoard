from flask import Blueprint, request
from flask_restx import Resource, Api
from .manager import compose, deleteCompose, getOnlineServices, getOfflineServices
from .ilo_manager import pushPower
import json

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

@api.route('/getServices')
class create(Resource):
    def get(self):
        return getOnlineServices() + getOfflineServices()

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

@api.route('/pushPower')
class pushPower(Resource):
    def get(self):
        pushPower()
        return 200