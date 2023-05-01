import requests
from rest_framework.exceptions import APIException
from rest_framework.status import is_success
from .models import Post

URL = "https://jsonplaceholder.typicode.com/posts"


def get_posts_from_api() -> list:
    response = requests.get(URL)
    if not is_success(response.status_code):
        raise APIException('внешняя апи недоступна')
    return response.json()


def save_to_db(posts: list) -> None:
    posts_for_save = []
    for post in posts:
        p = Post(
            id=post.get('id'),
            user_id=post.get('userId'),
            title=post.get('title'),
            body=post.get('body'),
            update_date=Post.update_date
        )
        posts_for_save.append(p)
    Post.objects.bulk_create(posts_for_save, ignore_conflicts=True)
    Post.objects.bulk_update(posts_for_save, ['user_id', 'title', 'body', 'update_date'])
    #     p = Post.objects.bulk_create([Post(user_id=post.get('userId'),
    #                                   title=post.get('title'),
    #                                   body=post.get('body'),
    #                                   update_date=Post.update_date
    #                                        )])
    #

