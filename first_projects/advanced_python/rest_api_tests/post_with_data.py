import requests

url = 'http://httpbin.org/post'
payload = {
    'website': 'dataquest.io',
    'courses': ['Python', 'SQL']
    }

r = requests.post(url, data=payload)
print(r.text)
