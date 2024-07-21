from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True, blank=True
    )
    level = models.PositiveSmallIntegerField(editable=False, default=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)


class Course(models.Model):
    COURSE_LEVELS = [(0, "Beginner"), (1, "Intermediate"), (2, "Expert")]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="courses"
    )
    level = models.PositiveSmallIntegerField(
        choices=COURSE_LEVELS, validators=[MinValueValidator(0), MaxValueValidator(2)]
    )
    price = models.PositiveSmallIntegerField(default=0)
    slug = AutoSlugField(blank=True, populate_from="title", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "course"
        get_latest_by = "created"

    def __str__(self):
        return self.title
