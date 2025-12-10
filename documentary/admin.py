from django.contrib import admin
from .models import Documentary
from book.widgets import AudioRecorderWidget


@admin.register(Documentary)
class DocumentaryModelAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "audio":
            kwargs["widget"] = AudioRecorderWidget
        return super().formfield_for_dbfield(db_field, request, **kwargs)
