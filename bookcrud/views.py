from .models import Book,  Favourite, UserFavouriteList
from .serializers import BookSerializer, FavouriteSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
# from django.contrib.auth.models import User


class CustomPagination(PageNumberPagination):
    # permission_classes = [IsAuthenticated]
    page_size_query_param = 'per_page'
    max_page_size = 100


class BookViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['bookTitle']

    def get_queryset(self):
        selectFav = self.request.query_params.get("favId", None)

        if selectFav == "0" or not selectFav:  
            queryset = Book.objects.all()
        else:
            # Filter books based on UserFavouriteList
            queryset = Book.objects.filter(
                id__in=UserFavouriteList.objects.filter(
                    favourite__id=selectFav
                ).values_list("book_id", flat=True)
            )
            # queryset = Book.objects.filter(
            #     id__in=UserFavouriteList.objects.filter(
            #         user=self.request.user, favourite__id=selectFav
            #     ).values_list("book_id", flat=True)
            # )

        return queryset.order_by('id')

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request })
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True, context={'request': request })
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, book_id=None, *args, **kwargs):
        FavId = self.request.query_params.get("favId", None)
        if FavId and book_id:
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
            if FavId == "0":
                if UserFavouriteList.objects.filter(book__id=book_id).exists():
                    UserFavouriteList.objects.get(book__id=book_id).delete()
            else:
                favourite_instance = Favourite.objects.get(id=FavId)
                if UserFavouriteList.objects.filter(book__id=book_id).exists():
                    UserFavouriteList.objects.filter(book__id=book_id).update(favourite=favourite_instance)
                else:
                    book_instance = Book.objects.get(id=book_id)
                    UserFavouriteList.objects.create(book=book_instance,favourite=favourite_instance)
            return Response(status=status.HTTP_200_OK)
        elif book_id and not FavId:
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(book, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED if not book_id else status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id=None, *args, **kwargs):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"detail": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    

class FavouriteViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, fav_id=None, *args, **kwargs):
        name = self.request.query_params.get("name", None)
        if fav_id and name:
            try:
                fav = Favourite.objects.get(id=fav_id)
            except Book.DoesNotExist:
                return Response({"detail": "Favourite not found."}, status=status.HTTP_404_NOT_FOUND)
            Favourite.objects.filter(id=fav_id).update(name=name)
            return Response(status=status.HTTP_200_OK)
        elif fav_id and not name:
            try:
                fav = Favourite.objects.get(id=fav_id)
            except Book.DoesNotExist:
                return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(fav, data=request.data)
        else:
            # request.data['user'] = User.objects.get(user=self.request.user)
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED if not fav_id else status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, fav_id=None, *args, **kwargs):
        try:
            fav = Favourite.objects.get(id=fav_id)
        except Book.DoesNotExist:
            return Response({"detail": "Favourite not found."}, status=status.HTTP_404_NOT_FOUND)
        fav.delete()
        return Response({"detail": "Favourite deleted successfully."}, status=status.HTTP_204_NO_CONTENT)