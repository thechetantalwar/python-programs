import json
import requests
url = ('http://newsapi.org/v2/top-headlines?country=us&apiKey=b2901f469e67460eb1f265f89a215f11')
response = requests.get(url)
data = response.json()
print (data['totalResults'])
