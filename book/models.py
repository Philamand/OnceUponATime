from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to="books/covers/")
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("book_detail", kwargs={"pk": self.pk})


class Page(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="books/images/")
    audio = models.FileField(upload_to="books/audio/", blank=True, null=True)
