import os
import json

def Cabecalho():
    os.system('cls')
    print(""" 
    ███████╗░█████╗░██╗░░██╗  ██████╗░███████╗██╗░░░██╗
    ██╔════╝██╔══██╗╚██╗██╔╝  ██╔══██╗██╔════╝██║░░░██║
    █████╗░░██║░░██║░╚███╔╝░  ██║░░██║█████╗░░╚██╗░██╔╝
    ██╔══╝░░██║░░██║░██╔██╗░  ██║░░██║██╔══╝░░░╚████╔╝░
    ██║░░░░░╚█████╔╝██╔╝╚██╗  ██████╔╝███████╗░░╚██╔╝░░
    ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝░░░╚═╝░░░
                ⍟  𝔖𝔦𝔰𝔱𝔢𝔪𝔞 𝔡𝔢 𝔪𝔞𝔰𝔰𝔞 𝔍𝔰𝔬𝔫 ⍟
    """)
    print("QA Online BR - EdsonSan")
    print("QA br Treinamento REST - API PRODUTOS COM JSOM DE 3 NÍVEIS")

def InicializaArquivo():
    dbprodutos_json = 'dbprodutos.json'
    diretorio_atual = os.listdir()
    if dbprodutos_json in diretorio_atual:
            print("Arquivo existe")
            with open('dbprodutos.json','r',encoding='utf-8') as dbprodutos:
                dados = json.load(dbprodutos)
                dbprodutos.close()       
                return dados
    else:
        print("Arquivo não Existe")
        exit
   

# def GravaArquivo(variavel):
#     atualizaArquivo = open('dbcursos.json','w')
#     atualizaArquivo.writelines(variavel)
#     # atualizaArquivo.  (variavel)
#     atualizaArquivo.close()       
    