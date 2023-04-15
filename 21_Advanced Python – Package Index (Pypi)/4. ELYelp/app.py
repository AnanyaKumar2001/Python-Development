# ******************------------- Getting Data From Yelp API
import requests
import config

client_ID = "zDxxDqQmvrMYf4n-M4M5kA"


api_url = "https://api.yelp.com/v3/businesses/search"


headers = {
    "Authorization": "Bearer " + config.api_key
}


params = {
    "term": "salon",
    "limit": 30,
    "location": "Miami"
}

response = requests.get(api_url, headers=headers, params=params)
businesses = response.json()["businesses"]

# for business in businesses:
#     print(business["name"])

names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
