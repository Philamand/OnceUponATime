import factory
from book.models import Book, Page


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence")
    cover = factory.django.ImageField()
    published = True


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page

    book = factory.SubFactory(BookFactory)
    text = factory.Faker("paragraph")
    image = factory.django.ImageField()
    audio = factory.django.FileField(filename="test.mp3")
