from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("books/<slug:slug>/", BookListView.as_view(), name="book_list_tag"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
]
