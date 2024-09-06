from src.coleta_dados import criar_dados_exemplo
from src.tratamento_dados import carregar_dados, limpar_dados, salvar_dados_tratados
from src.analise_dados import analise_exploratoria
from src.visualizacoes import criar_graficos
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from coleta_dados import criar_dados_exemplo

def executar_projeto():
    criar_dados_exemplo()

    dados = carregar_dados('data/dados_brutos.csv')
    dados_limpos = limpar_dados(dados)
    salvar_dados_tratados(dados_limpos)

    analise_exploratoria(dados_limpos)

    criar_graficos(dados_limpos)

if __name__ == '__main__':
    executar_projeto()
