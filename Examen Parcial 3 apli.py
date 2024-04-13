import requests

url = "https://127.0.0.1:8080"
response = requests.get(url)

if response.status_code == 200:
   data = response.json()
   print("hname")
   print("ip: ", data)
else:
    print("Error", response.text)