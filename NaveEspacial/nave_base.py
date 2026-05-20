from abc import ABC, abstractmethod
from tripulacao import PessoaTripulacao


class NaveBase(ABC):
    def __init__(self, nome, nivel_combstivel: float = 0, integridade_casco: float = 0):
        self.nome = nome 
        self.nivel_combustivel = nivel_combstivel # Combustivel vai de 0 a 100 L 
        self.status = True # Status deve ser bool, True para disponivel e False para não  
        self._tripulacao: list[PessoaTripulacao] = [] # lsita de passageiros da tripulação 
        self.integridad_casco = integridade_casco # Integridade do casco vai de 0% a 100%, tentar fazer um calculo de porcentagem em relação a qualidade do escudo.  
        
    @abstractmethod
    def preparar_para_decolagem(self):
        pass
    
    @property
    def tripulacao(self):
        return self._tripulacao
    
    def exibir_status (self):
        if self.status == True:
            print(f'Nave {self.nome} Pronta para Decolar')
    
    def adicionar_tripulante (self, tripulante: PessoaTripulacao):
        if isinstance(tripulante, PessoaTripulacao):
            if (tripulante not in self.tripulacao):
                self.tripulacao.append(tripulante)
            else: ValueError(f'Tripulante: {tripulante.nome}, Já Pertence a Tripulação Da Nave {self.nome}')
        else:
            ValueError(f'Pessoa não qualificada para ser da tripulação')
    
    def abastecer (self, valor: float):
        if self.nivel_combustivel == 0 and self.nivel_combustivel <= 100:
            self.nivel_combustivel =+ valor
        else: 
            raise ValueError('Combustível pode-ra transbordar')
        
