from enum import Enum
from typing import List

class Genero(Enum):
    ACTION = ("Action", "Ação")
    ADVENTURE = ("Adventure", "Aventura")
    ANIMATION = ("Animation", "Animação")
    COMEDY = ("Comedy", "Comédia")
    CRIME = ("Crime", "Crime")
    DOCUMENTARY = ("Documentary", "Documentário")
    DRAMA = ("Drama", "Drama")
    FAMILY = ("Family", "Família")
    FANTASY = ("Fantasy", "Fantasia")
    HISTORY = ("History", "História")
    HORROR = ("Horror", "Terror")
    MYSTERY = ("Mystery", "Mistério")
    MUSICAL = ("Musical", "Musical")
    ROMANCE = ("Romance", "Romance")
    SCI_FI = ("Sci-Fi", "Ficção Científica")
    THRILLER = ("Thriller", "Suspense")
    WAR = ("War", "Guerra")
    UNKNOWN = ("Unknown", "Desconhecido")
    
    def __init__(self, ingles: str, portugues: str) -> None:
        self.ingles = ingles 
        self.traducao = portugues 
        
        
    @classmethod    
    def converter_genero(cls, texto_api: str) -> List["Genero"]:
        if not texto_api:
            return [cls.UNKNOWN.traducao]
        
        partes = []
        for p in texto_api.split(','): # retiras as virgulas da lista
            partes.append(p.strip())# gaurda pedaços em uma lista e tira os eaços 
        
        resultado = []
        for parte in partes:
            for membro in cls:
                if membro.ingles.lower() == parte.lower():
                    resultado.append(membro.traducao)
                    break 
        return resultado
    
    
# ---------------------------



if __name__ == '__main__':
    texto_api = ""
    generos = Genero.converter_genero(texto_api)
    print(generos)