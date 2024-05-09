# Penser à installer requests, beautifulsoup4, html5lib avec pip install

import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette_ua/"

HEADERS = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def get_text_if_not_none(e):
    if e:
        return e.text.strip()
# text permet de renvoyer le contenu sans la balise
# strip permet de supprimer les espaces avant et après la chaine de caractères
    return None

response = requests.get(url, headers=HEADERS)
# response.encoding = "utf-8"
response.encoding = response.apparent_encoding

if response.status_code == 200:
    html = response.text
    # print(html)
    f = open("index.html", "w")
    f.write(html)
    f.close()
    
    soup = BeautifulSoup(html, "html5lib")
    
    # Titre
    titre = soup.find("h1").text
    print(titre)
    
    # Description
    description = get_text_if_not_none(soup.find("p", class_="description"))
    print(description)
    
    # Ingrédients  
    div_ingredients = soup.find("div", class_="ingredients")
    e_ingredients = div_ingredients.find_all("p")
    for e_ingredient in e_ingredients:
        print("INGREDIENT", e_ingredient.text)
    
    # Préparation
    table_preparation = soup.find("table", class_="preparation")
    e_etapes = table_preparation.find_all("td", class_="preparation_etape")
    for e_etape in e_etapes:
        print("ETAPES", e_etape.text)
    
    
    
else:
    print("ERREUR:", response.status_code)

print("FIN")