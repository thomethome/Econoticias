import pandas as pd

# Carregar as notícias do CSV
df = pd.read_csv("noticias.csv", encoding="utf-8")

# Criar estrutura HTML inicial
html_content = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoNotícias - OLixo.org</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 0; background-color: #f4f4f4; }
        h1 { text-align: center; color: #3498db; }
        h2 { text-align: center; color: #2c3e50; }
        .logo-container { text-align: center; margin: 20px 0; }
        .logo-container img { width: 200px; }
        ul { list-style-type: none; padding: 0; }
        li { background: white; margin: 10px; padding: 15px; border-radius: 5px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        a { text-decoration: none; font-weight: bold; color: #3498db; }
        a:hover { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>Bem-vindo ao OLixo.org – EcoNotícias!</h1>
    
    <div class="logo-container">
        <img src="logo.png" alt="OLixo.org">
        <h2>Transformando resíduos em oportunidades!</h2>
    </div>
    
    <h2>Últimas notícias sobre sustentabilidade</h2>
    <ul>
"""

# Controlar links da BBC para evitar duplicação
bbc_count = 0

for _, row in df.iterrows():
    if "bbc.com" in row["link"]:
        if bbc_count == 0:  # Permite apenas um link da BBC
            html_content += f'        <li><a href="{row["link"]}" target="_blank">{row["titulo"]}</a></li>\n'
            bbc_count += 1
    else:
        html_content += f'        <li><a href="{row["link"]}" target="_blank">{row["titulo"]}</a></li>\n'

html_content += """
    </ul>
</body>
</html>
"""

# Salvar o HTML final
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ Arquivo index.html atualizado com um link único da BBC, logo e melhor estilização!")
