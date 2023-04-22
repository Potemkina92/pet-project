from django.db import models


class Post(models.Model):
    user_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

