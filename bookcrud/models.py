from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    bookTitle  = models.CharField(("Book Title"),max_length=100,null=True,blank=True)

    bookAuthor  = models.CharField(("Book Author"),max_length=100,null=True,blank=True)

    bookYear  = models.CharField(("Book Year"),max_length=100,null=True,blank=True)

    createdDatetime = models.DateTimeField(auto_now_add=True)

    modifiedDatetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.bookTitle or '---'
    
class Favourite(models.Model):

    name  = models.CharField(("Name"),max_length=100,null=True,blank=True)

    createdDatetime = models.DateTimeField(auto_now_add=True)

    modifiedDatetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Favourite")
        verbose_name_plural = ("Favourites")

    def __str__(self):
        return self.name
    

class UserFavouriteList(models.Model):

    favourite = models.ForeignKey(Favourite, on_delete=models.CASCADE)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    createdDatetime = models.DateTimeField(auto_now_add=True)

    modifiedDatetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("User Favourite List")
        verbose_name_plural = ("User Favourite Lists")

    def __str__(self):
        return self.favourite.name