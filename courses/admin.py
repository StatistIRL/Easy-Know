from django.contrib import admin

from courses.models import Category, Course
from thumbnails.models import Thumbnail


class ThumbnailInline(admin.TabularInline):
    model = Thumbnail
    fields = ["original"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "level", "category"]
    inlines = [ThumbnailInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "level"]
