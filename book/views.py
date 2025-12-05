from typing import Any
from django.views.generic import ListView, DetailView
from .models import Book
from .services import get_book_pages


class BookListView(ListView):
    model = Book
    queryset = Book.objects.filter(published=True)
    context_object_name = "book_list"
    ordering = "title"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(get_book_pages(self.object))
        context["ip"] = self.request.META["REMOTE_ADDR"]
        return context
