import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

def criar_graficos(dados):
    plt.figure(figsize=(10, 6))
    sns.histplot(dados['renda'], bins=10, color='blue')
    plt.title('Distribuição de Renda')
    plt.xlabel('Renda')
    plt.ylabel('Frequência')
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.countplot(data=dados, x='escolaridade', palette='viridis')
    plt.title('Distribuição de Escolaridade')
    plt.xlabel('Escolaridade')
    plt.ylabel('Contagem')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == '__main__':
    dados = pd.read_csv('data/dados_tratados.csv')
    criar_graficos(dados)
