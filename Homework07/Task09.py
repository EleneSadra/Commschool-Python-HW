# #9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
# https://jsonplaceholder.typicode.com/todos
# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()

count = 0 

for todo in todos:
    if todo["completed"] == False:
        print(todo["title"])
        count += 1

print(f"Tasks not completed: {count}")    