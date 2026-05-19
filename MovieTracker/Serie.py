from dataclasses import dataclass,field 
from Temporada import Temporada
from Genero import Genero

@dataclass(slots=True)
class Serie:
     titulo: str 
     imdb: float
     visto: bool = False
     genero: list[Genero] = field(default_factory=list)
     temporada: list[Temporada] = field(default_factory=list)
    
     def adicionar_genero(self, genero: Genero):
        if genero not in self.genero:
            self.genero.append(genero)
            print(f'Genero {genero.name} adicionado ao filme {self.titulo}')
        else:
            print(f'Genero {genero.name}')
    
     def adicionar_temporada(self, temporada: Temporada):
        if temporada not in self.temporada:
            self.temporada.append(temporada)
            print(f'Temporada de {temporada.ano} adicionado ao filme {self.titulo}')
     
     def verificar_stado(self):
         for temporada in self.temporada:
             if temporada.verificar_stado() == True:
                 visto = True 
             else:
                 visto = False
             return visto 

                
        
     
