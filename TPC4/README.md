# TPC4: Analisador Léxico
## 2024-03-15
## Autor:
- A95338
- Maurício Miranda Pereira

# Resumo

Os tokens são elementos básicos da linguagem que o analisador léxico identifica. Neste caso, os tokens são palavras-chave (como SELECT, FROM, WHERE), identificadores (nomes de colunas e tabelas), números, operadores de comparação (>=, <=, >, <, =) e a vírgula (,). Cada token é definido com uma expressão regular correspondente.

O analisador ignora carateres de espaço em branco, tabulação e nova linha.

Cada token é definido por uma função que começa com t_ seguido pelo nome do token. Dentro dessas funções, as expressões regulares correspondentes são definidas para identificar o token.

Se um caráter inválido for encontrado, a função t_error é chamada para lidar com o erro e avançar para o próximo caráter.

A função principal do programa verifica se um argumento de linha de comando foi passado. Se sim, ele usa o argumento como a consulta SQL e executa o analisador léxico nessa consulta. Cada token identificado é impresso na saída padrão.
