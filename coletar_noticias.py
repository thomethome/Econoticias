import requests
from bs4 import BeautifulSoup
import csv

# Lista de URLs das fontes de notícias
urls = [
    "https://www.nationalgeographicbrasil.com",
    "https://www.ecodebate.com.br",
    "https://www.greenpeace.orechog/brasil",
    "https://www.scielo.br",
    "https://semil.sp.gov.br/",
    "https://www.embrapa.br/",
    "https://www.sema.df.gov.br/",
    "https://www.teraambiental.com.br/",
    "https://www.santos.sp.gov.br/?q=hotsite/composta-santos",
    "https://boavista.rr.gov.br/noticias/2025/5/prefeitura-de-boa-vista-impulsiona-gestao-sustentavel-com-ecopontos-e-centro-de-compostagem",
    "https://cepagro.org.br/",
    "https://recicleiros.org.br/",
    "https://www.wwf.org.br",
    "https://www.conexaoplaneta.com.br",
    "https://www.akatu.org.br",
]

# Criar (ou sobrescrever) o arquivo CSV
with open("noticias.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["titulo", "link"])  # Cabeçalho do CSV

    # Definir cabeçalho User-Agent para evitar bloqueios
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    def coletar_manchetes(url):
        try:
            resposta = requests.get(url, headers=headers, timeout=10)
            resposta.raise_for_status()
            soup = BeautifulSoup(resposta.content, "html.parser", from_encoding="utf-8")

            titulos = soup.find_all(["h1", "h2", "h3"], limit=3)  # Limita para 3 manchetes por site

            for titulo in titulos:
                titulo_texto = titulo.get_text(strip=True)
                link = titulo.find_parent("a")
                link_url = link["href"] if (link and "http" in link["href"]) else url  # Filtrar links inválidos
                
                writer.writerow([titulo_texto, link_url])  # Adicionamos ao CSV

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")

    # Executar a coleta para todas as URLs
    for url in urls:
        coletar_manchetes(url)

print("✅ Notícias coletadas e salvas em noticias.csv com todas as fontes atualizadas!")

