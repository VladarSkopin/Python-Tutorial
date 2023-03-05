import requests
from requests import Timeout

url = "http://httpbin.org/delay/10"

try:
    r = requests.get(url, timeout=3)
    print('Response Code:', r.status_code)
except Timeout as ex:
    print(ex)  # HTTPConnectionPool(host='httpbin.org', port=80): Read timed out. (read timeout=3)
