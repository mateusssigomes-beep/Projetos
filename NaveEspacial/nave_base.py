from abc import ABC, abstractmethod
from tripulacao import PessoaTripulaca


class Nave_Base(ABC):
    def __init__(self, nome, nivel_combstivel: float = 0, integridade_casco: float = 0):
        self.nome = nome 
        self.nivel_combustivel = nivel_combstivel # Combustivel vai de 0 a 100 L 
        self.status = True # Status deve ser bool, True para disponivel e False para não  
        self._tripulacao: list[PessoaTripulaca] = [] # lsita de passageiros da tripulação 
        self.integridad_casco = integridade_casco # Integridade do casco vai de 0% a 100%, tentar fazer um calculo de porcentagem em relação a qualidade do escudo.  
        
        
    @abstractmethod
    def preparar_para_decolagem():
        pass
    
    @property
    def tripulacao(self):
        return self._tripulacao
    
    def exibir_status (self,status):
        return self.nome, self.status
    
    def adicionar_tripulante (self, tripulante: PessoaTripulaca):
        if isinstance(tripulante, PessoaTripulaca):
            if (tripulante not in self.tripulacao):
                self.tripulacao.append(tripulante)
            else: ValueError(f'Tripulante: {tripulante}, Já Pertence a Tripulação Da Nave {self.nome}')
        else:
            ValueError(f'Pessoa não qualificada para ser da tripulação')