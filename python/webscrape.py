import json, urllib.request

r = urllib.request.urlopen('amazon.com')

data=json.load(r)

