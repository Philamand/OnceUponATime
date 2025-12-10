from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Documentary(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="documentaries/images/")
    text = models.TextField()
    audio = models.FileField(upload_to="documentaries/audio/", blank=True, null=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Documentaries"

    def __str__(self) -> str:
        return self.title
