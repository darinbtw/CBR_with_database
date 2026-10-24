import requests

url = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = url.json()

date = data['Date']
Nominal = data['Valute'][]