from abc import ABC, abstractmethod
from tripulacao import PessoaTripulacao


class NaveBase(ABC):
    def __init__(self, nome, nivel_combstivel: float = 0, integridade_casco: float = 0):
        self.nome = nome 
        self.nivel_combustivel = nivel_combstivel # Combustivel vai de 0 a 100 L 
        self.status = True # Status deve ser bool, True para disponivel e False para não  
        self._tripulacao: list[PessoaTripulacao] = [] # lsita de passageiros da tripulação 
        self.integridade_casco = integridade_casco # Integridade do casco vai de 0% a 100%, tentar fazer um calculo de porcentagem em relação a qualidade do escudo.  
        
    @abstractmethod
    def preparar_para_decolagem(self):
        pass
    
    @property
    def tripulacao(self):
        return self._tripulacao
    
    def exibir_status (self):
        if self.status:
            print(f'Nave {self.nome} Pronta para Decolar')
        else:
            print(f'Nave {self.nome} Não esta Pronta Para a Decolagem')
    
    def adicionar_tripulante (self, tripulante: PessoaTripulacao):
        if isinstance(tripulante, PessoaTripulacao):
            if (tripulante not in self.tripulacao):
                self.tripulacao.append(tripulante)
            else:
                raise ValueError(f'Tripulante: {tripulante.nome}, Já Pertence a Tripulação Da Nave {self.nome}')
        else:
            raise ValueError(f'Pessoa não qualificada para ser da tripulação')
    
    def abastecer (self, valor: float):
        if self.nivel_combustivel + valor > 100:
            raise ValueError('Cuidado Com o limite do combustivél')
        else:
            self.nivel_combustivel += valor
        
    def decolar(self):
        self.preparar_para_decolagem()
        self.status = True
        print('Nave esta disponível apra o lançamento')

    
    def pousar(self):
        self.preparar_para_decolagem()
        self.status  = False
        print(f'Nave esta pousando')
        
