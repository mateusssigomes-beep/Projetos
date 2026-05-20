from abc import ABC
from dataclasses import field 
from Genero import Genero
class Video(ABC):
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero 

