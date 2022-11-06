from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://en.wikipedia.org/wiki/Drake_(musician)').content
soup = BeautifulSoup(r, 'html.parser')
span = soup.find('span, {"class":"mw-headline" id="Discography')

print(span)

