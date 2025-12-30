# About this repo

This is an API-based blog I built to learn the basics of FastAPI. At the moment, there's no database. Posts live inside a Python list. 

## Blog storage
When viewing the main.py file, you can see the list that stores blog posts in the following code.

```python
# Storage for posts
posts: list[Post] = [ ]
```
## Dependencies
The `requirements.txt` file lists all the dependencies that Render must install to build the app.

## Python requests
Here's some code to show you how you might interact with this API via Python.

### Get posts
Want to see all posts and print out the titles? This code would do it:

```python
import requests

# This is the endpoint for getting posts
url = "https://fastapi-blog-4lg9.onrender.com/posts"

# The r variable stores the request as an object 
r = requests.get(url)

# The post variable turns the request into Python dictionaries so they're easy to work with
posts = r.json()

# This loop prints all post titles to the terminal
for i in posts:
    print(i['title'])
```
### Create a post
Feel like creating a new post? Check out this example code:

```python
import requests

# Get the API key
API_KEY = os.getenv("BLOG_API_KEY")

# You could paste this code into a new file, replace the payload with your own content,save the file with a .py extension, and run it in your computer's terminal.

# This line imports the Python requests module

# This is the endpoint for creating posts
url = "https://fastapi-blog-4lg9.onrender.com/posts"

# This adds the API key to the HTTP header, which is necessary for creating a post
headers = {
    "x-api-key": BLOG_API_KEY
}

# The payload is the content of your blog post, organized into three JSON key/value pairs
payload = {
    "title": "Another additional post",
    "content": "This is yet another post from example2.py",
    "published": True
}

# The r variable stores the request as an object
r = requests.post(url, json=payload, headers=headers)

# Post stores the request (r) as json
post = r.json()

# This prints some text in the terminal so you have the new post id
```



