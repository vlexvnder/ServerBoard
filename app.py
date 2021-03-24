from flask import Flask
from flask_restplus import Api
app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@api.route('/create')
class create(Resource)
    def get(self)
    

if __name__ == "__main__"
    app.run()