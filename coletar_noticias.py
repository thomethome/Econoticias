import feedparser
import csv

# Fonte única para testar
rss_url = "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml"

# Processar o feed RSS
feed = feedparser.parse(rss_url)

# Nome do arquivo CSV
arquivo_csv = "noticias.csv"

# Criar e abrir o arquivo CSV para escrita
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(["Título", "Link", "Data"])  # Cabeçalhos do CSV

    print("🔍 Coletando notícias ambientais e salvando no arquivo CSV...\n")

    if not feed.entries:
        print("⚠️ Nenhuma notícia encontrada.")
    else:
        for entry in feed.entries[:5]:  # Pegamos as 5 primeiras notícias
            titulo = entry.title
            link = entry.link
            data = entry.published if hasattr(entry, "published") else "Data não disponível"

            escritor_csv.writerow([titulo, link, data])  # Escrever no CSV

            print(f"✅ Título: {titulo}")
            print(f"🔗 Link: {link}")
            print(f"🗓 Data: {data}")
            print("-" * 40)

print("\n🎯 Coleta concluída! O arquivo `noticias.csv` foi gerado com sucesso.")

