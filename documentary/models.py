from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Documentary(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="documentaries/")
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
