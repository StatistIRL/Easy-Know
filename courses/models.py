from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Course(models.Model):
    COURSE_LEVELS = [(0, "Beginner"), (1, "Intermediate"), (2, "Expert")]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    level = models.PositiveSmallIntegerField(
        choices=COURSE_LEVELS, validators=[MinValueValidator(0), MaxValueValidator(2)]
    )
    price = models.PositiveSmallIntegerField()
    slug = AutoSlugField(blank=True, populate_from="title", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "course"
        get_latest_by = "created"

    def __str__(self):
        return self.title
