# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/Jack_Harlow').read()

# Make a soup 
soup = BeautifulSoup(source,'html5lib')
soup

# Extract the plain text content from paragraphs
paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))

# Extract text from paragraph headers
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

# Drop footnote superscripts in brackets
text = re.sub(r"\[.*?\]+", '', text)

# Replace '\n' (a new line) with '' and end the string at $1000.
text = text.replace('\n', '')[:-11]
print(text)