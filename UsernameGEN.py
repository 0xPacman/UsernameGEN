import random
import string
import requests

response = requests.get('https://randomuser.me/api/?results=10')

print(response.json()['results'][0]['name']['first'] + response.json()['results'][0]['name']['last'] + str(random.randint(0, 100)))
