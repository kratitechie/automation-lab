import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print (response.status_code)
data = response.json()

if response.status_code == 200:
    print ('data: ', response.json())
else:
    print ('data not found.')