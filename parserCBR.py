import requests
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2015'

def getCource(id):
    responce = requests.get(url)
    xml = BeautifulSoup(responce.content, 'html.parser')
    valute = xml.find('valute', {'id': id})
    name_valute = xml.find('name').text
    return f'(1 шт.) {name_valute} стоит(ят) {str(valute.value.text)} руб.'