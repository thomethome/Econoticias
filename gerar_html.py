import csv
from googletrans import Translator  # Biblioteca de tradução

# Inicializar tradutor
translator = Translator()

# Nome dos arquivos
arquivo_csv = "noticias.csv"
arquivo_html = "noticias.html"

# Criar um arquivo HTML com formatação correta
with open(arquivo_html, "w", encoding="utf-8") as arquivo:
    arquivo.write("<!DOCTYPE html>\n<html>\n<head>\n")
    arquivo.write("<meta charset='UTF-8'>\n<title>Últimas Notícias Ambientais</title>\n")
    arquivo.write("<style>\n")
    arquivo.write("iframe { width: 100%; height: 500px; border: none; margin-top: 20px; }\n")  # Estilo do iframe
    arquivo.write("</style>\n")
    arquivo.write("<script>\n")
    arquivo.write("function carregarNoticia(url) {\n")
    arquivo.write("    document.getElementById('noticia-frame').src = url;\n")
    arquivo.write("    document.getElementById('noticia-frame').style.display = 'block';\n")
    arquivo.write("}\n")
    arquivo.write("</script>\n")
    arquivo.write("</head>\n<body>\n")
    arquivo.write("<h1>Últimas Notícias Ambientais</h1>\n")
    arquivo.write("<ul>\n")

    # Ler os dados do CSV e traduzir as manchetes
    with open(arquivo_csv, "r", encoding="utf-8") as csvfile:
        leitor_csv = csv.reader(csvfile)
        next(leitor_csv)  # Pular cabeçalho
        
        for linha in leitor_csv:
            titulo_original, link, data = linha
            titulo_traduzido = translator.translate(titulo_original, dest="pt").text  # Traduz para PT
            
            # Criar link para carregar notícia dentro do iframe
            arquivo.write(f'    <li><a href="#" onclick="carregarNoticia(\'{link}\')">{titulo_traduzido}</a> - {data}</li>\n')

    arquivo.write("</ul>\n")
    arquivo.write("<iframe id='noticia-frame' style='display: none;'></iframe>\n")  # Adiciona um iframe invisível
    arquivo.write("</body>\n</html>\n")

print("\n🎯 Página `noticias.html` gerada com tradução e exibição das notícias corrigida!")

        
       