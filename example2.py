import requests
import os

# This code shows how you might use Python to create a new post. 

# You could paste this code into a new file, replace the payload with your own content,save the file with a .py extension, and run it in your computer's terminal.

# This line imports the Python requests module

# This is the endpoint for creating posts
url = "https://fastapi-blog-4lg9.onrender.com/posts"

# This adds the API key to the HTTP header, which is necessary for creating a post
headers = {
    "x-api-key": API_KEY
}

# The payload is the content of your blog post, organized into three JSON key/value pairs
payload = {
    "title": "One more additional post",
    "content": "This is yet another post from example2.py",
    "published": True
}

# The r variable stores the request as an object
r = requests.post(url, json=payload, headers=headers)

# Post stores the request (r) as json
post = r.json()

# This prints some text in the terminal so you have the new post id
print("Created post" , post['id'])

