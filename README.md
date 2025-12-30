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
