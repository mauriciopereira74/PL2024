# TPC2: Conversor de MD para HTML
## 2024-02-27
## Autor:
- A95338
- Maurício Miranda Pereira

# Resumo

Este código converte um arquivo Markdown em HTML. Começamos definindo o arquivo Markdown a ser convertido e o arquivo HTML de saída. Em seguida, estabelecemos padrões de expressões regulares para identificar e substituir elementos Markdown por HTML, como cabeçalhos, negrito, itálico, listas ordenadas, links e imagens.

A função convert_to_html aplica essas substituições ao texto do arquivo Markdown, processando cada linha individualmente. Durante o processamento, as listas ordenadas são identificadas e as tags <ol> e </ol> são adicionadas conforme necessário.

Por fim, o conteúdo HTML processado é escrito no arquivo de saída. Em suma, o código lê um arquivo Markdown, aplica substituições para converter elementos Markdown em HTML e salva o HTML resultante em um novo arquivo.
