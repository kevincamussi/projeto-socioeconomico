import pandas as pd

def carregar_dados(caminho_arquivo):
    dados = pd.read_csv(caminho_arquivo)
    return dados

def limpar_dados(dados):
    dados_limpos = dados.dropna().drop_duplicates()
    return dados_limpos

def salvar_dados_tratados(dados):
    dados.to_csv('data/dados_tratados.csv', index=False)
    print("Dados tratados salvos em 'data/dados_tratados.csv'")

if __name__ == '__main__':
    dados = carregar_dados('data/dados_brutos.csv')
    dados_limpos = limpar_dados(dados)
    salvar_dados_tratados(dados_limpos)
