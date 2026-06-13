# #7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და
# დაბეჭდე პირველი მომხმარებლის სახელი.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(users[0]["name"])