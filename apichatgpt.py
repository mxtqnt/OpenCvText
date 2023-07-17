from senha import API_KEY
import requests
import json

headers = {'Authorization': f'Bearer {API_KEY}'}
link = 'https://api.openai.com/v1/models'
requisicao = requests.post(link, headers)

print(requisicao)
print(requisicao.text)