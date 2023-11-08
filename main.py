import requests
import networkx as nx 
import matplotlib as plt
import json
import sys


api = 'https://api.nhtsa.gov'

endpoint = '/SafetyRatings/modelyear/2013/make/Honda/model/Accord'


response = requests.get(api+endpoint)

data = response.json()

print (data)
### returns list of dictionaries 

