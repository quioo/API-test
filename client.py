import requests
import json

url = "http://127.0.0.1:5000/matricula"

data = {
    'ra': '9329894',
    'nome': 'João',
    'idade': '16'   
}

response = requests.post(url, json=data)

print('Status Code:', response.status_code)
print('Response Json:', response.json())
