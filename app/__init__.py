from flask import Flask

app = Flask(__name__, template_folder="template")
app.config["DEBUG"] = True
app.config['image_dir'] = "images/"

from app import api
from app import spa

app.run()