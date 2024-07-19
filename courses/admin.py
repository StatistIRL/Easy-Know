from django.contrib import admin

from courses.models import Category, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "level", "category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "level"]
