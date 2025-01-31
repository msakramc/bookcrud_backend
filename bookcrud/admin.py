from django.contrib import admin
from bookcrud.models import Book,Favourite,UserFavouriteList


# Register your models here.
admin.site.register(Book)
admin.site.register(Favourite)
admin.site.register(UserFavouriteList)