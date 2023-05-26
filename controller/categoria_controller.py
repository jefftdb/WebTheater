from app import app
from flask import render_template
from model.categoria_model import CategoriaModel
from model.videos_model import Videos_model


@app.route("/")
def home():
    
    return render_template("home.html", todasCategorias = CategoriaModel().categorias)

@app.route("/estaCategoria.html/<id>")
def EstaCategoria(id):

    if int(id) < 0 or int(id) > len(CategoriaModel().categorias):
        return render_template("naoencontrado.html", nome = 'Categoria')
    else:
        return render_template("estaCategoria.html", id= id, EstaCategoria = CategoriaModel().EstaCategoria(int(id)), VideosDestaCategoria = Videos_model().VideosDestaCategoria(int(id)))
    
