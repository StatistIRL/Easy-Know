from django.db import models
from .mixins import ModelDiffMixin


class Thumbnail(ModelDiffMixin, models.Model):
    course = models.OneToOneField(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="thumbnail",
        blank=True,
        null=True,
    )
    original = models.ImageField()
    big = models.ImageField(blank=True, null=True)
    medium = models.ImageField(blank=True, null=True)
    small = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = "thumbnail"
