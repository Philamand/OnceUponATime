from typing import Dict, Any
from django.db.models.query import QuerySet
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


def get_book_list_queryset(queryset: QuerySet[Book], tag: str | None) -> QuerySet[Book]:
    """
    Returns a queryset for the BookList view.
    """

    queryset = queryset.filter(published=True)

    if tag:
        queryset = queryset.filter(tags__slug=tag)

    return queryset
