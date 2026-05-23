#que deve ser lançada quando se tenta realizar operações em módulos sem suporte de vida ativo ou com recursos críticos não resolvidos. A exceção deve aceitar uma mensagem descritiva.
class ModuloIndispoNIvel(Exception):
    def __init__(self,menasgem):
        super().__init__(menasgem)
        
    