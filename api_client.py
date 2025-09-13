import requests

URL_PHOTOS = "https://jsonplaceholder.typicode.com/photos"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments"

def get_photos():
    return requests.get(URL_PHOTOS)

def get_posts():
    return requests.get(URL_POSTS)

def get_comments():
    return requests.get(URL_COMMENTS)
