# Importamos la librería para hacer peticiones http
import requests
# Importamos la librería para "enterder" el html
from bs4 import BeautifulSoup

import csv
from datetime import datetime


# Definimos la url que queremos pedir
url_page = 'https://www.ambito.com/contenidos/merval.html'

# tarda 480 milisegundos
page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

# Hacemos la petición
# tabla = soup.find('table', attrs={'id': 'table'})
tabla = soup.find('tr', attrs={'td': ''})
print(tabla)
