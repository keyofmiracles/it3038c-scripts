import json
import requests

r = requests.get("http://localhost:3000")

data=r.json()


widget = (data[0]['name'])
color = (data[0]['color'])

widget1 = (data[1]['name'])
color1 = (data[1]['color'])

widget2 = (data[3]['name'])
color2 = (data[2]['color'])

widget3 = (data[3]['name'])
color3 = (data[3]['color'])


print(widget  + " is " + color)
print(widget1  + " is " + color1)
print(widget2 + " is " + color2)
print(widget3  + " is " + color3)