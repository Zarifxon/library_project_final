from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)



    def validate(self, data):
        title = data.get('title', "").strip()
        author = data.get('author', None).strip()
        if not title or not all(char.isalnum() or char.isspace() for char in title):
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi harflardan tashkil topgan bo'lishi kerak!"
                }
            )

        # elif not title.isalpha():
        #     raise ValidationError(
        #         {
        #             "status": False,
        #             "message": "Kitob sarlavhasi harflardan tashkil topgan bo'lishi kerak!"
        #         }
        #     )
        # check title and author from datatabese existance

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni kirita olmaysiz"
                }
            )

        return data

    # def validate_price(self, price):
    #     if price is not None and (price < 0 or price > 9999999):
    #         raise ValidationError(
    #             {
    #                 "status": False,
    #                 "message": "Narx noto'g'ri kiritilgan"
    #             }
    #         )
    #
# ModelSerializer vs Serializer

# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length=150)
#     output = serializers.CharField(max_length=120)
