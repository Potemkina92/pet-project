from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
         {'fields': ('id', 'name', 'username', 'email')
          }),
        ('Address',
         {
          'fields': ('street', 'suite', 'city', 'zipcode')
          }),
        ('Geo',
         {'fields': [('lat', 'lng')]}),
        (None,
         {'fields': ('phone', 'website')}),
        ('Company',
         {'fields': ('company_name', 'catchPhrase', 'bs')})
    )


@admin.register(Post)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('update_date', )
