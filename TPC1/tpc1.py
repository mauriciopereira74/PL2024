import pandas as pd
import numpy as np

# Leitura do CSV
df = pd.read_csv('emd.csv')

# Lista ordenada alfabeticamente das modalidades desportivas
modalidades_ordenadas = sorted(df['modalidade'].unique())

# Percentagens de atletas aptos e inaptos para a prática desportiva
total_atletas = len(df)
aptos = df['federado'].sum()
inaptos = total_atletas - aptos
percent_aptos = (aptos / total_atletas) * 100
percent_inaptos = 100 - percent_aptos

# Ajustar os intervalos dos escalões de idade para '[20,24]', '[25,29]', '[30,34]', '[35,39]'
idades_bins = [20, 25, 30, 35, 40]
df['escalao_etario'] = pd.cut(df['idade'], bins=idades_bins, right=False)

# Contagem de atletas por escalão etário
contagem_escaloes = df['escalao_etario'].value_counts().sort_index().to_dict()

# Formatando os intervalos corretos de idade
formatted_contagem_escaloes = {
    f'[{interval.left},{interval.right - 1}]': count
    for interval, count in contagem_escaloes.items()
}

# Exibindo os resultados
print("Lista ordenada alfabeticamente das modalidades desportivas:")
print(modalidades_ordenadas)
print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
print(f"Atletas aptos: {percent_aptos:.2f}%")
print(f"Atletas inaptos: {percent_inaptos:.2f}%")
print("\nDistribuição de atletas por escalão etário:")
print(formatted_contagem_escaloes)
