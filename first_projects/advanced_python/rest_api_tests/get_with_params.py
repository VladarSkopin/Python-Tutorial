import requests

# GET with parmeters (after "?" in URL):
url = 'http://httpbin.org/get'
payload = {
    'website': 'dataquest.io',
    'courses': ['Python', 'SQL']
    }

r = requests.get(url, params=payload)
print(r.text)
