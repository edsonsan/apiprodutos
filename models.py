from typing import Optional, Dict
from pydantic import BaseModel

class Especificacoes(BaseModel):
    tela: str
    processador: str
    memoria: str
    armazenamento: str

class Detalhes(BaseModel):
    marca: str
    preco: float
    estoque: int
    especificacoes: Especificacoes

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: Detalhes