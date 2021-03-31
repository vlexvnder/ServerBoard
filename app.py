from flask import Flask, request
from manager import compose, deleteCompose
from apis import blueprint as api
import client/client

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(client, url_prefix='/')

if __name__ == "__main__":
    app.run()
