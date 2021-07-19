from flask import Flask, request
import json
from backend.apis import blueprint as api
from client.client import client

app = Flask(__name__)

SECRET_KEY = "no this is not my actual key"

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(client, url_prefix='/')

config_file_path = 'config/config.json'

with open(config_file_path) as f:
    config = json.load(f)

app_ip = config['app_ip']

if __name__ == "__main__":
    app.run(host=app_ip)
