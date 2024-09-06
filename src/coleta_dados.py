import pandas as pd

def criar_dados_exemplo():
#obs: dados para simulação apenas, mudar para os dados coletados !!
    dados = {
        'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
        'idade': [25, 34, 45, 23, 35],
        'renda': [1500, 2200, 3000, 1200, 2000],
        'escolaridade': ['Ensino Médio', 'Superior Completo', 'Ensino Médio', 'Ensino Fundamental', 'Ensino Médio'],
        'emprego': ['Desempregado', 'Empregado', 'Autônomo', 'Desempregado', 'Empregado']
    }
    
    df = pd.DataFrame(dados)
    df.to_csv('data/dados_brutos.csv', index=False)
    print("Dados de exemplo criados e salvos em 'data/dados_brutos.csv'")
    
if __name__ == '__main__':
    criar_dados_exemplo()
