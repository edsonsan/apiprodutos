from itertools import count
from tokenize import String
from typing import Dict, List, Optional
from fastapi import FastAPI, responses
from fastapi import HTTPException
from fastapi import status
import os
import json
import util
from models import Produto, Detalhes, Especificacoes

global dbprodutos_json

util.Cabecalho()

# dbprodutos=util.InicializaArquivo()
dbprodutos: Dict[str, Produto] = util.InicializaArquivo()
app = FastAPI(title="QA br Treinamento REST - API PRODUTOS COM JSOM DE 3 NÍVEIS",  
              version= "1.0.0",         
              description="QAonline BR")
print("")

# print(dbprodutos)
print("*"*40)
contador_id = max(int(k) for k in dbprodutos.keys()) + 1 if dbprodutos else 1
print(contador_id)

# Rota para retornar Todos os produtos
@app.get('/produtos', response_model=Dict[str,Produto],
         summary="Retorna todos os Produtos",
         description="Retorna todos os Produtos",
         response_description="Produtos retornados com SUCESSO.") 
async def get_listaprodutos():
    return dbprodutos

# Rota para retornar Produto pelo o ID
@app.get('/produtos/{produto_id}', 
         description="Retorna o Produto do ID informado",
         summary="Retorna Curso pelo IDs",
         response_model=Produto)
async def get_idproduto(produto_id: str):
    if produto_id not in dbprodutos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    return dbprodutos[produto_id]

# Rota para inserir novos produtos
@app.post("/produtos", response_model=Produto, status_code=status.HTTP_201_CREATED)
async def adicionar_produto(produto: Produto):
    global contador_id
    produto_id = str(contador_id)
    produto.id = contador_id  # Atribui o ID incremental ao produto
    dbprodutos[produto_id] = produto
    contador_id += 1  # Incrementa o contador para o próximo ID
    return produto

# Rota para atualizar um produto existente
@app.patch("/produtos/{produto_id}", response_model=Produto)
async def atualizar_produto(produto_id: str, produto: Produto):
    if produto_id not in dbprodutos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    produto.id = produto_id
    dbprodutos[produto_id] = produto
    return produto

# Rota para deletar um produto pelo ID
@app.delete("/produtos/{produto_id}", response_model=Produto)
async def deletar_produto(produto_id: str):
    if produto_id not in dbprodutos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    produto_deletado = dbprodutos.pop(produto_id)
    return produto_deletado