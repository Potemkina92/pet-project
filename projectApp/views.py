from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response as RestResponse
from projectApp.utils import get_posts_from_api, save_to_db, get_users_from_api, saveUser


class PostApiView(APIView):
    def get(self, request):
        posts = get_posts_from_api()
        save_to_db(posts)
        return RestResponse(status=status.HTTP_200_OK, data={'status': 'ok'})


class UserApiView(APIView):
    def get(self, request):
        users = get_users_from_api()
        saveUser(users)
        return RestResponse(status=status.HTTP_200_OK, data={'status': 'ok'})