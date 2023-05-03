from django.contrib import admin
from .models import *


@admin.register(Post)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('update_date', )
