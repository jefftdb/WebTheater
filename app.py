from flask import Flask,render_template
import os

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

from controller.categoria_controller import *
from controller.video_controller import *