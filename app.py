from flask import Flask, request
from flask_restplus import Resource, Api
from manager import compose, deleteContainer
app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@api.route('/create')
class create(Resource):
    def post(self):
        compose(request.form['name'])
        return 200
@api.route('/remove')
class remove(Resource):
    def post(self):
        deleteContainer(request.form['id'])
        return 200

        
    

if __name__ == "__main__":
    app.run()
