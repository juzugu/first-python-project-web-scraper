import requests
from bs4 import BeautifulSoup
urljob = "https://co.computrabajo.com/trabajos-de-python-en-cali"
urlresponse = requests.get(urljob)