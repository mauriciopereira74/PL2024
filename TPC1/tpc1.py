import pandas as pd
import numpy as np

# Ler o arquivo CSV
df = pd.read_csv('emd.csv')

# Lista ordenada alfabeticamente das modalidades desportivas
modalidades_ordenadas = sorted(df['modalidade'].unique())

# Percentagens de atletas aptos e inaptos para a prática desportiva
percentagem_apto = (df['resultado'].sum() / len(df)) * 100
percentagem_inapto = 100 - percentagem_apto

# Ajustar os intervalos dos escalões de idade para 0-4 anos, 5-9 anos, 10-14 anos, etc.
idades_bins = np.arange(0, df['idade'].max() + 6, 5) - 1
escaloes_etarios = pd.cut(df['idade'], bins=idades_bins, include_lowest=True, right=False)

# Contagem de atletas por escalão etário
contagem_escaloes = pd.Series(escaloes_etarios).value_counts(sort=False)

# Exibindo os resultados
print("Lista ordenada alfabeticamente das modalidades desportivas:")
print(modalidades_ordenadas)

print("\nPercentagens de atletas aptos e inaptos:")
print(f"Apto: {percentagem_apto:.2f}%")
print(f"Inapto: {percentagem_inapto:.2f}%")

print("\nDistribuição de atletas por escalão etário:")
# Exibir os intervalos corretos de idade
print(contagem_escaloes.to_string())
