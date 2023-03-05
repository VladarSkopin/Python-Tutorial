import requests

# To update an existing resource with a new data (will completely replace the existing values):

api_url = "https://jsonplaceholder.typicode.com/todos/10"  # 10 = id of "todo"
response = requests.get(api_url)
print(response.json())  # {'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())  # {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
