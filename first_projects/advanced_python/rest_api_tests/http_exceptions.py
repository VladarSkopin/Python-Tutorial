import requests
from requests import HTTPError

url = "http://httpbin.org/status/404"
try:
    r = requests.get(url)
    r.raise_for_status()
    print('Response Code:', r.status_code)
except HTTPError as ex:
    print(ex)  # 404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
