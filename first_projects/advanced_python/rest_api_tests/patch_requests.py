import requests

# To modify the value of a specific field on an existing resource

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}   # only the title will be replaced
response = requests.patch(api_url, json=todo)
response.json()  # {'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}

print(response.status_code)  # 200
