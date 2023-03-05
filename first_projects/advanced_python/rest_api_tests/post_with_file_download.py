import requests

myurl = 'https://httpbin.org/post'
files = {'file': ('test1.txt', 'File upload test using Requests')}
getdata = requests.post(myurl, files=files)
print(getdata.text)
