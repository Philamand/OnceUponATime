from typing import Dict, Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Book


def get_book_pages(book: Book) -> Dict[str, Any]:
    """
    Returns a Book's pages data for the Detail View.
    """

    pages: list[dict[str, str | dict[str, str]]] = [
        {"image": book.cover.url, "text": book.title}
    ]

    for index, page in enumerate(book.page_set.order_by("id"), start=1):
        audio: dict[str, str] | None = None
        if page.audio:
            audio = {"id": f"audio-{index}", "url": page.audio.url}
        pages.append(
            {
                "image": page.image.url,
                "text": page.text,
                "audio": audio,
            }
        )

    return {"pages": pages}


def get_book_list_queryset(
    request: HttpRequest, queryset: QuerySet[Book]
) -> QuerySet[Book]:
    """
    Returns all public books and the user's custom book if the user is authenticated.
    Return only public books if the user is not authenticated.
    """
    queryset = queryset.filter(published=True)

    if request.user.is_authenticated:
        queryset = queryset.filter(Q(owner=request.user) | Q(owner=None))
    else:
        queryset = queryset.filter(Q(owner=None))

    return queryset
