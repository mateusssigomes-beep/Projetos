from postoenum import PostoEnum
from tripulacao import PessoaTripulaca
from nave_base import Nave_Base


if __name__ == ('__main__'):
    try:
        tripulante1 = PessoaTripulaca(nome = 'Mateus', posto = PostoEnum.ALMIRANTE, idade = 50, experiencia_anos= 30)
        
        tripulante2 = PessoaTripulaca(nome= 'Rosa', posto= PostoEnum.SARGENTO, idade= 65, experiencia_anos= 50)
        print(f'{tripulante1}\n\n{tripulante2}')
    except ValueError as ve:
        print(ve)
    
    