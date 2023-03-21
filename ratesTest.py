import requests

url = "https://api.apilayer.com/fixer/convert?to=EUR&from=GBP&amount=1"

payload = {}
headers= {
  "apikey": "gvAREzrnVgThuDDGwYX2cArgtXf4Ol8f"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)