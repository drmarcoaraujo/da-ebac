# código de geração do gráfico

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler os dados do arquivo CSV em um DataFrame do pandas
df = pd.read_csv('gasolina.csv')

# Configuração do tema do Seaborn
sns.set_theme()

# Criação do gráfico de linhas
plt.figure(figsize=(10, 6))  # Ajustando o tamanho

# Cria o gráfico de linhas usando Seaborn
sns.lineplot(data=df, x='dia', y='venda')

# Adicionando título e rótulos nos eixos em negrito
plt.title('Gráfico de Linhas: Preço da Gasolina ao Longo do Tempo', fontweight='bold')
plt.xlabel('Dia', fontweight='bold')
plt.ylabel('Preço (R$)', fontweight='bold')

# Calculando mediana, Q1 e Q3 dos preços
mediana = df['venda'].median()
q1 = df['venda'].quantile(0.25)
q3 = df['venda'].quantile(0.75)

# Adicionando linhas horizontais pontilhadas para mediana, Q1 e Q3
plt.axhline(y=mediana, color='blue', linestyle='--', linewidth=1, label='Mediana')
plt.axhline(y=q1, color='green', linestyle='--', linewidth=1, label='Q1')
plt.axhline(y=q3, color='red', linestyle='--', linewidth=1, label='Q3')

# Colocando os textos das linhas no gráfico
plt.text(df['dia'].max(), mediana, f'Mediana: {mediana:.2f}', color='blue', ha='right', va='bottom')
plt.text(df['dia'].max(), q1, f'Q1: {q1:.2f}', color='green', ha='right', va='bottom')
plt.text(df['dia'].max(), q3, f'Q3: {q3:.2f}', color='red', ha='right', va='bottom')

# Adicionando a legenda ao gráfico
plt.legend()

# Salvando o gráfico
plt.savefig('gasolina.png')

# Mostra o gráfico
plt.show()