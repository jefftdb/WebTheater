
from model.entity.categoria import Categoria


class CategoriaModel:

    def __init__(self):
        
        aventura = Categoria(0,"Aventura","Filmes de aventura", "aventura_banner.jpg")
        ficcao = Categoria(1,"Ficção","Filmes de ficção", "ficcao_banner.jpg")
        terror = Categoria(2,"Terror","Filmes de Terror", "terror_banner.jpg")
        romance = Categoria(3,"Romance","Filmes de Romance", "romance_banner.jpg")
        
        self.categorias = [aventura,ficcao,terror,romance]


    
    def EstaCategoria(self,id):

        for EstaCategoria in self.categorias:
            if EstaCategoria.id == id:
                categoriaCerta = EstaCategoria
        
        return categoriaCerta










