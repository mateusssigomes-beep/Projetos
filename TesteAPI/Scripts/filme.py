from dataclasses import dataclass
from dataclasses import field
from operator import attrgetter
from Genero import Genero
from video import Video
from typing import List

class Filme(Video):

    def __init__(self, titulo, diretor, ano, imdb_rating=None):  # Corrigido: imdb_ratting -> imdb_rating para consistência
        super().__init__(titulo, imdb_rating)
        self.diretor = diretor
        self.ano = ano
        
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        if value < 1895:
            print("O ano de lançamento do filme deve ser maior ou igual a 1895.")
        self._ano = value

    def reproduzir(self):
        print(f"Reproduzindo o filme '{self.titulo}'...")
        self.visto = True

    def __str__(self):
        return f"Filme: {self.titulo} | Diretor: {self.diretor} | Ano: {self.ano} | IMDb: {self.imdb_rating} | Gêneros: {self.lista_generos}"

