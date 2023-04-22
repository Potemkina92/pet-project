from django.contrib.sites import requests
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import Response
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
import requests
from projectApp.models import Post
# from projectApp.serializers import PostSerializer
from rest_framework.response import Response as RestResponse

from projectApp.utils import get_posts_from_api, save_to_db


def index(request):
    return HttpResponse("Hello World!")


class PostApiView(APIView):
    def get(self, request):
        posts = get_posts_from_api()
        save_to_db(posts)
        return RestResponse(status=status.HTTP_200_OK, data={'status': 'ok'})


        # r = requests.get("https://jsonplaceholder.typicode.com/posts")
        # for i in r:
        #     i = Post.objects.create(
        #         user_id=request.data['user_id'],
        #         title=request.data['title'],
        #         body=request.data['body']
        #     )


        # serializer = PostSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()


    #
    # def post(self, request):
    #     lst = Post.objects.create(
    #         userId=request.data['userId'],
    #         id=request.data['id'],
    #         title=request.data['title'],
    #         body=request.data['body']
    #     )

# class ApiView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class GetPostsList(APIView):
#     def get(self, request, format=None):
#         r = requests.get("https://jsonplaceholder.typicode.com/posts")
#         return HttpResponse(r)
#


def savePost(postData):
    post = Post()
    post.userId = postData['userId']
    post.id = postData['id']
    post.title = postData['title']
    post.body = postData['body']

    post.save()
