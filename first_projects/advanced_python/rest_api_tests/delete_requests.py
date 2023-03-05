import requests

# To completely remove a resource

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())  # {}

print(response.status_code)  # 200
