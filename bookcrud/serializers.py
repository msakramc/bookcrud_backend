from rest_framework import serializers
from .models import Book, Favourite, UserFavouriteList

class BookSerializer(serializers.ModelSerializer):
    favId = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_favId(self, obj):
        favId = list(
            Favourite.objects.filter(
                id__in=UserFavouriteList.objects.filter(book=obj).values_list("favourite__id", flat=True)
            ).values_list("id", flat=True)
        )
        if favId:
            return favId[0]
        else:
            return None
        


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'