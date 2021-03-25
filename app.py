from flask import Flask
from flask_restplus import Api
from create import createContainer
app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@api.route('/create')
class create(Resource):
    def post(self):
        createContainer(request.form['name'])
        return 200

        
    

if __name__ == "__main__":
    app.run()