from postoenum import PostoEnum
from tripulacao import PessoaTripulacao
from naveguerra import NaveGuerra
from missaoinvalidaerror import MissaoInvalidaError

if __name__ == '__main__':

    print('=' * 50)
    print('TESTE 1 — Criando tripulantes válidos')
    print('=' * 50)
    try:
        capitao = PessoaTripulacao(nome='Mateus', posto=PostoEnum.CAPITAO, idade=40, experiencia_anos=18)
        tenente = PessoaTripulacao(nome='Rosa', posto=PostoEnum.TENENTE, idade=30, experiencia_anos=10)
        cabo = PessoaTripulacao(nome='João', posto=PostoEnum.CABO, idade=22, experiencia_anos=2)
        print(capitao)
        print('')
        print(tenente)
        print('')
        print(cabo)
    except ValueError as ve:
        print(f'[ERRO] {ve}')

    print()
    print('=' * 50)
    print('TESTE 2 — Tripulante com idade inválida (menor de 18)')
    print('=' * 50)
    try:
        menor = PessoaTripulacao(nome='Lucas', posto=PostoEnum.CABO, idade=16, experiencia_anos=0)
    except ValueError as ve:
        print(f'[ERRO ESPERADO] {ve}')

    print()
    print('=' * 50)
    print('TESTE 3 — Tripulante com experiência maior que a possível')
    print('=' * 50)
    try:
        invalido = PessoaTripulacao(nome='Ana', posto=PostoEnum.SARGENTO, idade=25, experiencia_anos=20)
    except ValueError as ve:
        print(f'[ERRO ESPERADO] {ve}')

    print()
    print('=' * 50)
    print('TESTE 4 — Criando NaveGuerra com capitão válido')
    print('=' * 50)
    try:
        nave = NaveGuerra(nome='Estrela Negra', nivel_combstivel=90, capitao=capitao, integridade_casco=80)
        print(f'Nave criada: {nave.nome}')
        if nave.capitao:
            print(f'Capitão: {nave.capitao.nome}')
        print(f'Combustível: {nave.nivel_combustivel}')
        print(f'Tripulação: {[t.nome for t in nave.tripulacao]}')
    except MissaoInvalidaError as me:
        print(f'[ERRO] {me}')

    print()
    print('=' * 50)
    print('TESTE 5 — Tentando definir capitão com posto insuficiente (CABO)')
    print('=' * 50)
    try:
        nave.capitao = cabo
    except MissaoInvalidaError as me:
        print(f'[ERRO ESPERADO] {me}')

    print()
    print('=' * 50)
    print('TESTE 6 — Adicionando tripulantes e preparando para decolagem')
    print('=' * 50)
    try:
        nave.adicionar_tripulante(tenente)
        nave.adicionar_tripulante(cabo)
        print(f'Tripulação atual: {[t.nome for t in nave.tripulacao]}')
        nave.preparar_para_decolagem()
    except (MissaoInvalidaError, ValueError) as e:
        print(f'[ERRO] {e}')

    print()
    print('=' * 50)
    print('TESTE 7 — Decolagem com combustível insuficiente')
    print('=' * 50)
    try:
        nave_vazia = NaveGuerra(nome='Fragata', nivel_combstivel=50, capitao=capitao)
        nave_vazia.preparar_para_decolagem()
    except MissaoInvalidaError as me:
        print(f'[ERRO ESPERADO] {me}')

    print()
    print('=' * 50)
    print('TESTE 8 — Abastecendo nave')
    print('=' * 50)
    try:
        nave_vazia.abastecer(40)
        print(f'Combustível após abastecimento: {nave_vazia.nivel_combustivel}')
        nave_vazia.abastecer(20)  # deve estourar o limite
    except ValueError as ve:
        print(f'[ERRO ESPERADO] {ve}')

    print()
    print('=' * 50)
    print('TESTE 9 — Ativando e desligando escudos')
    print('=' * 50)
    try:
        nave.ativar_escudos()
        nave.desligar_escudos()
    except MissaoInvalidaError as me:
        print(f'[ERRO] {me}')

    print()
    print('=' * 50)
    print('TESTE 10 — Tentando adicionar tripulante duplicado')
    print('=' * 50)
    try:
        nave.adicionar_tripulante(tenente)
    except ValueError as ve:
        print(f'[ERRO ESPERADO] {ve}')
