class Retangulo:
    def __init__(self, largura: float, altura: float):
        self.largura = largura 
        self.altura = altura 
        
        
    @property
    def largura(self):
        return (f'{self._largura:.1f}cm')

    @largura.setter
    def largura(self, valor: float):
        if valor < 0:
            raise ValueError('Vlores nagaticos não são permitidos')
        self._largura = valor 
        
        
    @ property
    def altura(self):
        return (f'{self._altura:.1f}cm')   
    
    @altura.setter
    def altura(self, valor: float):
        self._altura = valor 
        
        
    def calcular_area(self):
        area  = self._altura * self._largura
        return print(f'Resultado da conta {area:.2f}cm')      

ret1 = Retangulo(3,2)

print(ret1.altura)
print(f"{ret1.largura} Atributo da classe no que seria a property ")
print(f'{ret1._largura} variável retornada do getter/setter')
ret1.calcular_area()