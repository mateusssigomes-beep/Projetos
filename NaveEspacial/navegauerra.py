from sistemadedefesamixin import SistemaDeDefesaMixin
from nave_base import NaveBase
from tripulacao import PessoaTripulacao
from postoenum import PostoEnum
from missaoinvalidaerror import MissaoInvalidaError

class NaveGuerra(SistemaDeDefesaMixin, NaveBase):
    def __init__(self, nome, nivel_combstivel: float = 0, capitao: PessoaTripulacao | None = None, integridade_casco: float = 0):
        super().__init__(nome, nivel_combstivel, integridade_casco)
        self._capitao = None
        if capitao is not None:
            self.capitao = capitao 
        
    @property
    def capitao(self):
        return self._capitao
    
    @capitao.setter
    def capitao(self, pessoa: PessoaTripulacao):
        if (pessoa.posto.value < PostoEnum.TENENTE.value):
            raise MissaoInvalidaError(f'Missao invalida pessoa {pessoa.nome} como capitão o posto dele é {pessoa.posto.name}.')
        if self._capitao is not None and self._capitao in self.tripulacao:
            self.tripulacao.remove(self._capitao)
        self._capitao = pessoa 
        try: 
            self.adicionar_tripulante(pessoa)
        except ValueError:
            pass
        
    def preparar_para_decolagem(self):
        if self.nivel_combustivel > 80 and self.tripulacao and self.capitao:
            print('Nave Pronta para decolagem')
        else:
            raise MissaoInvalidaError('Invalido na decolagem.')
        
        
        
        