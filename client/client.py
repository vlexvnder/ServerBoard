from flask import Blueprint, render_template

client = Blueprint("client", __name__, 
    template_folder="templates", 
    static_folder="static", 
    static_url_path="/client/static" 
)

@client.route("/")
def index():
    return render_template("index.html")