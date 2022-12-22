import requests

url = 'https://cmic.solvenergy.com/cmicprod/ap-rest-api/rest/1/apvendor'

headers = {
    "accept": "application/json",
    "authorization": "Basic Y2hhZC5ldmVucnVkOldhdGVycG9sbzEh"
}

response = requests.get(url, headers=headers)

print(response.text)
