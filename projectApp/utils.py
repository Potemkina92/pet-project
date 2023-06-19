import requests
from rest_framework.exceptions import APIException
from rest_framework.status import is_success
from .models import Post, User

URL = "https://jsonplaceholder.typicode.com/posts"
URL_users = "https://jsonplaceholder.typicode.com/users"


def get_posts_from_api() -> list:
    response = requests.get(URL)
    if not is_success(response.status_code):
        raise APIException('внешняя апи недоступна')
    return response.json()


def save_to_db(posts: list) -> None:
    posts_for_save = []
    for post in posts:
        p = Post(
            id=post['id'],
            title=post['title'],
            body=post['body'],
            update_date=Post.update_date
        )
        posts_for_save.append(p)
    Post.objects.bulk_create(posts_for_save, ignore_conflicts=True)
    Post.objects.bulk_update(posts_for_save, ['user', 'title', 'body', 'update_date'])


def get_users_from_api() -> list:
    response = requests.get(URL_users)
    if not is_success(response.status_code):
        raise APIException('внешняя апи недоступна')
    return response.json()


def saveUser(users: list) -> None:
    users_for_save = []
    for user in users:
        u = User(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email'],
            street=user['address']['street'],
            suite=user['address']['suite'],
            city=user['address']['city'],
            zipcode=user['address']['zipcode'],
            lat=user['address']['geo']['lat'],
            lng=user['address']['geo']['lng'],
            phone=user['phone'],
            website=user['website'],
            company_name=user['company']['name'],
            catchPhrase=user['company']['catchPhrase'],
            bs=user['company']['bs'],
        )
        users_for_save.append(u)

    User.objects.bulk_create(users_for_save, ignore_conflicts=True)
    User.objects.bulk_update(users_for_save, ['name', 'username', 'email', 'street', 'suite', 'city',
                                              'zipcode', 'lat', 'lng', 'phone', 'website', 'company_name',
                                              'catchPhrase',
                                              'bs'])
