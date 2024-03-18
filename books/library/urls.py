from django.urls import path
from .views import LibraryDetailView, LibraryLISTView


urlpatterns = [
    path('lib-list/', LibraryLISTView.as_view(), name='list-books'),
    path('lib-detail/<slug:book_slug>/', LibraryDetailView.as_view(), name='library'),

]
