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
```




