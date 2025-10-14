from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    genero: str
    quantidade: int = 1
