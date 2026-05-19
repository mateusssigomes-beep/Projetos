from dataclasses import dataclass
from datetime import date

@dataclass (slots=True)
class Capitulo:
    titulo: str 
    numero: int
    quantidade_capitulos: int
    data_capitulo: date = date.today() 
    visto = bool = False
    