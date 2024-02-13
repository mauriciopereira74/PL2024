# TPC1: Exames Médicos Desportivos
## 2024-02-09
## Autor:
Maurício Miranda Pereira
A95338

# Procedimento

Leitura e Estruturação dos Dados:
A primeira etapa consiste na leitura de um ficheiro CSV, transformando as suas linhas numa estrutura tabular organizada. Cada linha representa um atleta, e colunas específicas são definidas para capturar informações cruciais, como idade, modalidade desportiva e resultado da avaliação.

Conversão de Tipos de Dados:
Garantindo a integridade dos dados, o código converte colunas-chave, como 'idade' e 'resultado', para tipos apropriados. Esta etapa promove a consistência dos dados, permitindo análises mais precisas.

Exploração das Modalidades Desportivas:
É gerada uma lista alfabética das modalidades desportivas únicas, proporcionando uma visão abrangente das atividades atléticas representadas no conjunto de dados. Isso facilita a compreensão da diversidade de práticas desportivas envolvidas.

Avaliação da Aptidão dos Atletas:
Calcula-se a percentagem de atletas aptos e inaptos com base nos resultados da avaliação. Estas métricas oferecem uma visão instantânea do estado geral de aptidão dos participantes, fornecendo insights cruciais para estratégias de treinamento e acompanhamento.

Ajuste de Escalões Etários:
O código define intervalos específicos para os escalões etários, agrupando os atletas em faixas de cinco anos. Esta abordagem detalhada destaca a distribuição de idades, permitindo uma compreensão mais profunda da demografia dos participantes.

Contagem de Atletas por Escalão Etário:
Utilizando os intervalos definidos, o código calcula a contagem de atletas em cada faixa etária. Esta análise demográfica ajuda a identificar padrões e tendências relacionadas à idade dos participantes.