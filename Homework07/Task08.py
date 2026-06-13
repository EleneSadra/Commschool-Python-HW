# #8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
# შექმენი ახალი პოსტი შემდეგი მონაცემებით:
# {"title": "Test", "body": "Hello World", "userId": 5}

import requests

new_post = {"title": "Test", "body": "Hello World", "userId": 5}

response = requests.post("https://jsonplaceholder.typicode.com/posts")

print(response.json())