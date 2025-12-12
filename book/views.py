from typing import Any
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from .models import Book
from .services import get_book_pages


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    ordering = "title"
    paginate_by = 6

    def get_queryset(self) -> QuerySet[Book]:
        queryset: QuerySet[Book] = super().get_queryset().filter(published=True)

        return queryset

    def get_template_names(self):
        template: list[str] = super().get_template_names()
        if self.request.META.get("HTTP_HX_REQUEST"):
            template = ["book/components/book_list.html"]

        return template


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context.update(get_book_pages(self.object))

        return context
