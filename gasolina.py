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

# Adicionando título e rótulos nos eixos
plt.title('Gráfico de Linhas: Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvando o gráfico
plt.savefig('gasolina.png')

# Mostra o gráfico
plt.show()