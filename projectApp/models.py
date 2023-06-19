from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # # address = {
    street = models.CharField(max_length=1000)
    suite = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=1000)
    # geo = {
    lat = models.DecimalField(decimal_places=4, max_digits=8)
    lng = models.DecimalField(decimal_places=4, max_digits=8)
    # }}
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    # company = {
    company_name = models.CharField(max_length=100, default="")
    catchPhrase = models.CharField(max_length=100)
    bs = models.CharField(max_length=100)
    # }}

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

