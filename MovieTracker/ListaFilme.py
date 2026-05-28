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
    
 
    
    def reproduzir(self):
        print(f"Reproduzindo o filme '{self.titulo}'...")
        self.visto = True
    
    # def __str__(self):
    #     generos_str = ", ".join([g.name for g in self.lista_generos]) if self.lista_generos else "Nenhum"
    #     return f"Filme: {self.titulo} | Diretor: {self.diretor} | Ano: {self.ano} | IMDb: {self.imdb_rating} | Gêneros: {generos_str}"