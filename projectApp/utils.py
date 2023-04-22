import requests
from rest_framework.exceptions import APIException
from  rest_framework.status import is_success
from .models import Post

URL = "https://jsonplaceholder.typicode.com/posts" #вытащитьпеременнуювcongigfile


def get_posts_from_api() -> list:
    response = requests.get(URL)
    if not is_success(response.status_code):
        raise APIException('внешняя апи недоступна')
    return response.json()


def save_to_db(posts: list) -> None:
    for post in posts:
        p = Post(
            user_id=post.get('userId'),
            title=post.get('title'),
            body=post.get('body'),
            update_date=
        )
        p.save()
