import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()  # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

print(response.status_code)  # 201
