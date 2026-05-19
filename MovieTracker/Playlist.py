from dataclasses import dataclass, field
from ListaFilme import Filme

@dataclass
class Playlist:
    nome: str
    descricao: str
    filmes: list[Filme]  = field(default_factory = list)
    
    def adicionar_filme(self, filme):
        if filme not in self.filmes:
            self.filmes.append(filme)
        else:
            print('Filme já esta adicionado na lista')

    def remover_filme(self, filme):
        if filme in self.filmes:
            self.filmes.remove(filme)
            print(f'Filme {filme.titulo} removido da Playlist>')
        else:
            print("Filme não encontrado na playlist.")
    
    