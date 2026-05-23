
class RecursoModulo:
    def __init__(self, recurso: str, quantidade_atual: float = 0 , limite_critico: float = 0):
        self.recurso = recurso 
        self._quantidade_atual = quantidade_atual
        self._limite_critico = limite_critico
        
        
    @property
    def quantidade_atual(self):
        return self._quantidade_atual
    
    @quantidade_atual.setter #Deve retornar o valor atual que tem em estoque do recurso expecificado
    def quantidade_atual(self, quantidade):
        if self.quantidade_atual > 100:
            raise ValueError ('Valores incorretos')
        else: 
            self._quantidade_atual += quantidade
   
   
   
   
    # def quantidade_atual (self, valor):
    #     if self._quantidade_atual + valor > 100:
    #         raise ValueError (f'Quantidade de {self.recurso} Acima do limite')
    #     self._quantidade_atual += valor 
        
        
        
        
        

    @property
    def limite_critico(self):
        return self._limite_critico
    
    @limite_critico.setter # seta o limite que o reservatório de recursos pode conter
    def limite_critico(self):
        pass
    
    
    
    
    
    
    
    # def limite_critico (self, nivel = 30):
    #     if self._quantidade_atual < nivel:
    #         raise ValueError('Quantidade abaixo do limite')
    #     self._limite_critico = self.quantidade_atual