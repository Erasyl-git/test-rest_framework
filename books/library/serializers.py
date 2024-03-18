from rest_framework import serializers
from .models import Library


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ('heading', 'display_heading', 'author', 'style', 'year_of_publication', 'slug')


