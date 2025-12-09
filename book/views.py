from typing import Any
from django.views.generic import ListView, DetailView
from .models import Book
from .services import get_book_pages, get_book_list_queryset


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    ordering = "title"

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.kwargs.get("slug")

        return get_book_list_queryset(queryset, tag)

    def get_template_names(self):
        template = super().get_template_names()
        if self.request.META.get("HTTP_HX_REQUEST"):
            template = ["book/components/book_list.html"]

        return template


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(get_book_pages(self.object))

        return context
