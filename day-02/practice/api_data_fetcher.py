import requests

API_KEY = "65621b20f83f8d94d1519cecb8ac3d70" # Step 1 get API key

url = "https://v3.football.api-sports.io/leagues" # Step 2 find a base URL

payload={}
headers = {
  'x-apisports-key': '65621b20f83f8d94d1519cecb8ac3d70',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)