import requests

# This code shows how you might use Python to get all existing blog posts. 

# This is the endpoint for getting posts
url = "https://fastapi-blog-4lg9.onrender.com/posts"

# The r variable stores the request as an object 
r = requests.get(url)

# The post variable turns the request into Python dictionaries so they're easy to work with
posts = r.json()

# This loop prints all post titles to the terminal
for i in posts:
    print(i['title'])




