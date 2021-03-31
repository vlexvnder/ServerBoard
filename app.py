from flask import Flask, request
from backend.apis import blueprint as api
from client.client import client

app = Flask(__name__)

SECRET_KEY = b'1$\xfbs\x88\xaf\xd3\xf7;\xb0v\x97Xe\x19\xa6'

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(client, url_prefix='/')

config_file_path = 'config/config.json'

with open(config_file_path) as f:
    config = json.load(f)

app_ip = config['app_ip']

if __name__ == "__main__":
    app.run(host=app_ip)
