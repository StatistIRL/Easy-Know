from django.contrib import admin

from thumbnails.models import Thumbnail

# Register your models here.


@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ["id", "original"]
