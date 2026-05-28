from dataclasses import field
from Genero import Genero
from abc import ABC, abstractmethod

class Video(ABC):
    def __init__(self, titulo, imdb_rating=None):
        self.titulo = titulo
        self.lista_generos = []
        self.imdb_rating = imdb_rating
        self.visto = False

    def adicionar_genero(self, genero: Genero):
        if genero not in self.lista_generos:
            self.lista_generos.append(genero)
            # print(f"Genero adciionado")  

    @property
    def imdb_rating(self):
        return self._imdb_rating
    
    @imdb_rating.setter
    def imdb_rating(self, value):
        if value is not None and (value < 0 or value > 10):
            print("A avaliação do IMDb deve ser entre 0 e 10.")
        else:
            self._imdb_rating = value

    @property
    def visto(self):    
        return self._visto
    
    @visto.setter
    def visto(self, value):
        if not isinstance(value, bool):
            print("O valor de 'visto' deve ser um booleano (True ou False).")
        else:
            self._visto = value

    def verificar_estado(self):
        return self.visto

    @abstractmethod
    def reproduzir(self):
        pass