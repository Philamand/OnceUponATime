from django.contrib import admin
from .models import Book, Page, Tag
from .widgets import AudioRecorderWidget


admin.site.register(Book)


@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "audio":
            kwargs["widget"] = AudioRecorderWidget
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
