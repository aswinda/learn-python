import requests, json

payload = {'params' : 'coba'}
resp = requests.post('http://127.0.0.1:8000/endpoint', payload)
print(resp)
