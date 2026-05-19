from dataclasses import dataclass
from Videos import Video
from Genero import Genero

@dataclass
class Filme(Video):
    ano: int
    diretor: str
    visto: bool = False
    generos = []

    def __post_init__(self):
        if self.ano <= 1895:
            print(f"O ano do filme deve ser maior que 1895, mas foi fornecido: {self.ano}")
    
    def adicionar_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
            print(f'Genero {genero.name} adicionado ao filme {self.titulo}')
        else:
            print(f'Genero {genero.name}')
        # if self.visto 
    
 
