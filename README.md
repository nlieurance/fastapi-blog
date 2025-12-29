# About this repo

This is an API-based blog I built to learn the basics of FastAPI. At the moment, there's no database. Posts live inside a Python list. 

## Blog storage
When viewing the main.py file, you can see the list that stores blog posts in the fololwing code.

```python
# Storage for posts
posts: list[Post] = [ ]
```
