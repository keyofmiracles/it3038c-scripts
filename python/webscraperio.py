from cgitb import text
from dis import dis
import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Drake_(musician)").content

soup = BeautifulSoup(r, 'html.parser')
span = soup.find("span", {"id":"Discography"})
span2 = soup.findAll("b", {re.compile('($0)')})



disco = span.text
print(disco)
print(span2)

#mw-content-text > div.mw-parser-output > p:nth-child(187) > b