from django.test import TestCase
from book.services import get_book_pages
from .factories import BookFactory, PageFactory
import json


class BookPagesServiceTest(TestCase):
    def setUp(self):
        self.book = BookFactory()
        self.pages = PageFactory.create_batch(2, book=self.book)

    def test_returns_correct_structure(self):
        data = get_book_pages(self.book)
        self.assertEqual(len(data["audios"]), 2)
        self.assertEqual(data["audios"][0]["id"], "audio-1")
        self.assertIn(".mp3", data["audios"][0]["url"])

        pages = json.loads(data["pages"])
        self.assertEqual(len(pages), 3)
