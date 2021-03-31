from flask import Flask, request
from manager import compose, deleteCompose
from apis import blueprint as api

app = Flask(__name__)
app.register_blueprint('api', url_prefix='/api/')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
