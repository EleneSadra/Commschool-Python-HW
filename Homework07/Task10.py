# #10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ
# იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
# "Post Title – Author Name"

# გამოიტანე მხოლოდ პირველი 5

import requests

posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
users = requests.get("https://jsonplaceholder.typicode.com/users").json()

users_dict = {}
for user in users:
    users_dict[user["id"]] = user["name"]

for post in posts:
    author = users_dict[post["userId"]]
    print(f"{post["title"]} - {author}")