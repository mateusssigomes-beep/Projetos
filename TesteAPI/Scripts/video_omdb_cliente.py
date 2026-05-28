from gerenciador import GerenciadorAPI
from filme import Filme
from Genero import Genero




class VideoOmdbCliente():
   
    def __init__(self, titulo, api_key):
        self.api_key = api_key
        self.titulo = titulo
        self.dados_api = None 

    def obter_dados_api(self):
        #Lê os dados da API usando o GerenciadorAPI e armazena em self.dados_api    
        gerenciador = GerenciadorAPI(self.api_key)
        gerenciador.configurar(self.titulo)
        self.dados_api = gerenciador.obter_dados()
        generos = self.dados_api.get("Genre", "")
        titulo = self.dados_api.get("Title", "")
        imdbrating = float (self.dados_api.get("imdbRating", ""))
        ano = int (self.dados_api.get("Year", ""))
        diretor = self.dados_api.get("Director","")
        generos_enum = Genero.converter_genero(generos)
        filme = Filme(titulo, diretor, ano, imdbrating)
        for genero in generos_enum:
            filme.adicionar_genero(genero)
        return filme
        
        
        
if __name__ == '__main__':
    obterdados = VideoOmdbCliente('Terminator', '4123d0c1')
    filme = obterdados.obter_dados_api()
    print(filme)