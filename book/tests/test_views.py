from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .factories import BookFactory, PageFactory


class BookListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser", password="TestPassword"
        )
        self.published = BookFactory.create_batch(3, published=True)
        self.unpublished = BookFactory.create_batch(2, published=False)
        self.private = BookFactory.create_batch(2, published=True, owner=self.user)

    def test_returns_only_public_published_books(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context["book_list"]), 3)

        for book in response.context["book_list"]:
            self.assertTrue(book.published)

    def test_returns_private_books(self):
        self.client.login(username="TestUser", password="TestPassword")

        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context["book_list"]), 5)


class BookDetailViewTest(TestCase):
    def setUp(self):
        self.book = BookFactory()
        self.pages = PageFactory.create_batch(2, book=self.book)

    def test_get_detail_view(self):
        response = self.client.get(reverse("book_detail", kwargs={"pk": self.book.pk}))
        self.assertEqual(response.status_code, 200)

        self.assertIn("pages", response.context)
        self.assertIn("book", response.context)
