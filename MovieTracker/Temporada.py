from dataclasses import dataclass, field 
from Capitulo import Capitulo
@dataclass
class Temporada:
    ano: int 
    capitulos: list[Capitulo] = field(default_factory=list)
    visto = False
    
    def adicionar_capitulos(self, capitulo: Capitulo):
        if capitulo not in self.capitulos:
            self.capitulos.append(capitulo)
            print(f'Capitulo {capitulo.titulo} adicionado a temporada do ano {self.ano}')
            
            
    def verificar_stado(self):
          for capitulo in self.capitulos:
              if capitulo.visto:
                  visto = True 
              else:
                 visto = False
                 break
            