from postoenum import PostoEnum

class PessoaTripulacao():
    def __init__(self, nome: str, posto: PostoEnum, idade: int, experiencia_anos: int ):
        self.nome = nome 
        self.posto = posto
        self.idade = idade  # setter 
        self.experiencia_anos = experiencia_anos # setter 
        
        
    
    @property # getter 
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor: int):
        if(valor < 18):
            raise ValueError(f'Passageiros com menos de 18 anos não podem fazer parte da tripulação, Idade informada: {valor}')
        else:
            self._idade = valor
           

    @property # getter 
    def experiencia_anos(self):
        return self._experiencia_anos
    
    @experiencia_anos.setter
    def experiencia_anos(self, valor):
        if valor > self.idade - 1:
            raise ValueError(
                'EXP maior que tempo de vida do tripulante'
                f'Idade:{self.idade}, Exp:{valor}')
        else:
            self._experiencia_anos = valor 
            
    
    def __repr__(self):
        return(f'Nome Do Tripulante: {self.nome}\nIdade do Tripulante: {self.idade} Anos\nPosto do Tripulante: {self.posto.name}\nExp do Tripulante: {self.experiencia_anos} Anos ')
        