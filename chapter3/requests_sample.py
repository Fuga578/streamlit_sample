import requests


url = "https://www.aozora.gr.jp/cards/000160/files/3368_ruby_25107.zip"
response = requests.get(url)

print(response.status_code)
print(len(response.content))
print(type(response.content))
