from typing import Dict, Any
from .models import Book


def get_book_pages(book: Book) -> Dict[str, Any]:
    """
    Returns a Book's pages data for the Detail View.
    """

    pages = [{"image": book.cover.url, "text": book.title}]

    for index, page in enumerate(book.page_set.order_by("id"), start=1):
        audio = None
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
