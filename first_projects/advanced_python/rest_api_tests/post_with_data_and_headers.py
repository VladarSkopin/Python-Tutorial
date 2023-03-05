import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()
# {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

print(response.status_code)  # 201
