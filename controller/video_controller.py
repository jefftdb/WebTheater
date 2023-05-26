from app import app
from flask import render_template
from model.videos_model import *



@app.route('/ExibeVideo.html/<id>')
def ExibeVideo(id):
    return render_template('ExibeVideo.html',id = id, esteVideo = Videos_model().EsteVideo(id) )
        