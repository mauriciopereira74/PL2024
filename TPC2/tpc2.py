import re
import sys

def convert_to_html(md):
    # Expressões regulares para substituir os elementos Markdown por HTML
    replacements = {
        r'^# (.+)$': r'<h1>\1</h1>',
        r'^## (.+)$': r'<h2>\1</h2>',
        r'^### (.+)$': r'<h3>\1</h3>',
        r'\*\*(.+?)\*\*': r'<b>\1</b>',
        r'\*(.+?)\*': r'<i>\1</i>',
        r'^1\. (.+)$': r'<li>\1</li>',
        r'^!\[(.*?)\]\((.*?)\)$': r'<img src="\2" alt="\1"/>',
        r'\[(.*?)\]\((.*?)\)': r'<a href="\2">\1</a>'
    }

    # Processa cada linha do markdown aplicando as substituições
    html = ""
    for line in md.split('\n'):
        for pattern, replacement in replacements.items():
            line = re.sub(pattern, replacement, line)
        
        # Adiciona as tags <ol> e </ol> para listas ordenadas
        if re.match(r'^1\. ', line):
            if not html.endswith('<ol>'):
                html += '<ol>'
            html += line + '\n'
        elif html.endswith('<ol>'):
            html += '</ol>'
        
        # Adiciona a linha ao conteúdo HTML
        html += line + '\n'

    # Verifica se ainda há uma lista ordenada aberta e fecha-a, se necessário
    if html.endswith('<ol>'):
        html += '</ol>'
    
    # Envolvendo todo o conteúdo em uma tag <p>
    html = '<p>' + html + '</p>'
    
    return html

def main(md_file, html_file):
    # Lê o conteúdo do arquivo Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Converte o conteúdo do Markdown para HTML
    html_content = convert_to_html(md_content)

    # Escreve o conteúdo HTML no arquivo de saída
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python markdown_to_html.py <input_md_file> <output_html_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
