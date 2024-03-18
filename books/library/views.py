from django.shortcuts import get_object_or_404
from .models import Library
from .serializers import LibrarySerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView


class LibraryLISTView(ListAPIView):
    serializer_class = LibrarySerializer

    def get_queryset(self):
        return Library.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LibraryDetailView(RetrieveAPIView):

    queryset = Library.objects.all()
    serializer = LibrarySerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        books = get_object_or_404(self.queryset, slug=self.kwargs['book_slug'])
        seralizer = self.serializer(books)
        return Response(seralizer.data)


