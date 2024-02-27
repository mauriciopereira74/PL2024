# TPC3: Somador on/off
## 2024-02-27
## Autor:
- A95338
- Maurício Miranda Pereira

# Resumo

O código processa um arquivo de texto em busca de sequências de dígitos para somá-las. Ele segue as seguintes etapas:

Leitura do Arquivo: O arquivo especificado é lido e seu conteúdo é armazenado em uma variável chamada text.

Inicialização de Variáveis: Duas variáveis são inicializadas: sum_enabled controla se a soma está ativada ou desativada, e total armazena o resultado da soma atual.

Padrão de Expressão Regular: É definido um padrão de expressão regular que corresponde a três tipos de padrões: a palavra "on" ou "off" em qualquer combinação de maiúsculas e minúsculas, sequências de um ou mais dígitos e o caractere "=".

Processamento do Texto: O texto é percorrido em busca de correspondências com o padrão definido.

Controle do Estado da Soma: Quando a palavra encontrada é "on", a variável sum_enabled é definida como True, indicando que a soma está ativada. Quando a palavra é "off", sum_enabled é definida como False e o total é resetado para zero.

Soma dos Dígitos: Se a soma está ativada e a correspondência atual é uma sequência de dígitos, esse número é adicionado ao total.

Impressão do Resultado: Se a soma está ativada e a correspondência atual é "=", o total acumulado até o momento é impresso, indicando o resultado da soma.

Em resumo, este código percorre um texto, soma as sequências de dígitos encontradas e imprime o resultado quando encontra o caractere "=", respeitando os comandos "On" e "Off" para ligar e desligar a soma.
