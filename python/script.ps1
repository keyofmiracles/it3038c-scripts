python .\searchwiki.py

import wikipedia

var = input("Enter search string")

page_content = wikipedia.page(var).content
# outputs the text content of the "Parsec" page on wikipedia
print(page_content)

with open('wikipage.txt', 'w', encoding='utf-8') as f:
    f.writelines(page_content)