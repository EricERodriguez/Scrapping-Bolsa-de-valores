# Importamos la librería para hacer peticiones http
import requests
# Importamos la librería para "enterder" el html
from bs4 import BeautifulSoup

import csv
from datetime import datetime


# Definimos la url que queremos pedir
url_page = 'https://iol.invertironline.com/mercado/cotizaciones'

# tarda 480 milisegundos
page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

# Hacemos la petición
tabla = soup.find('table', attrs={'id': 'cotizaciones'})
# tabla = soup.find('tr', attrs={'td': ''})
# print(tabla.find_all('b'))
nombre = tabla.select('b')
# print((nombre[1].text).replace('\S', ''))


# print(tabla.select('Maximo'))
maximoPorAccion = soup.find_all('td', attrs={'data-field': 'Maximo'})

maxAcci = []
maxAcciFloat = []
nameAcci = []
for i in  range(0, len(maximoPorAccion)):
    maxAcci.append((((((maximoPorAccion[i].text).replace('\n', '')).replace('\r', '')).replace(' ', '')).replace(".", "")).replace(",","."))
    maxAcciFloat.append(float(maxAcci[i]))
    nameAcci.append((((nombre[i].text).replace('\n', '')).replace('\r', '')).replace(' ', ''))

ind = maxAcciFloat.index(max(maxAcciFloat))
print(max(maxAcciFloat))
print(nameAcci[ind])

