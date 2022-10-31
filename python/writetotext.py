import wikipedia

var = input("Enter search string: ")
var = str(var)
try:
    contents = wikipedia.page(var, auto_suggest=False).content
    print(contents)

    with open('wikipage.txt', 'w', encoding='utf-8') as f:
        f.write(contents)
    
    
except wikipedia.exceptions.DisambiguationError as list:
    print(list)
    nextinput = input("Oops, which " + var + " were you referring to? Type it in here: ")
    altcontent = wikipedia.WikipediaPage(nextinput).section("Discography")
    print(altcontent)

 
 

