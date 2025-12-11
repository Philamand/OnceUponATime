from typing import Any
from django.views.generic import ListView
from django.db.models.query import QuerySet
from .models import Documentary


class DocumentaryListView(ListView):
    model = Documentary
    context_object_name = "documentary_list"
    ordering = "title"

    def get_queryset(self) -> QuerySet[Documentary]:
        return super().get_queryset().filter(published=True)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context["disable_autoplay"] = True

        return context
