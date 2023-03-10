import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers ={
    "Authorization" : "Bearer " + config.api_key
}

params = {
    "term" : "Barber",
    "location" : "NYC"
}

response = requests.get(url, headers=headers, params=params, timeout=10)
businesses = response.json()["businesses"]
# print(businesses)
names = [business["name"] for business in businesses if business["rating"] > 4.5]
for business in businesses:
    print(business["name"])
print(names)
