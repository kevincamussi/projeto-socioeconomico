import pandas as pd
import numpy as np

def analise_exploratoria(dados):
    resumo = dados.describe()  
    correlacao = dados.corr(numeric_only=True)  
    print("Resumo dos Dados:\n", resumo)
    print("Correlação entre variáveis numéricas:\n", correlacao)

if __name__ == '__main__':
    dados = pd.read_csv('data/dados_tratados.csv')
    analise_exploratoria(dados)
