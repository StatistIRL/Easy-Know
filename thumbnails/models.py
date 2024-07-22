from django.conf import settings
from django.db import models
from PIL import Image
from thumbnails.utils import get_upload_path
from .mixins import ModelDiffMixin

class Thumbnail(ModelDiffMixin, models.Model):
    course = models.OneToOneField(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="thumbnail",
        blank=True,
        null=True,
    )
    original = models.ImageField(upload_to=get_upload_path)
    big = models.ImageField(blank=True, null=True)
    medium = models.ImageField(blank=True, null=True)
    small = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        models.Model.save(self, *args, **kwargs)
        if self.get_field_diff("original"):
            self.create_thumbnails()
            super().save(*args, **kwargs)

    def create_thumbnails(self):
        base_path = self.original.path
        img = Image.open(base_path)
        for info in settings.THUMBNAIL_SIZES:
            name, width, height = info.values()
            file_postfix = f"_{name}_{width}x{height}.webp"
            full_path = f"{base_path.rsplit('.', 1)[0]}{file_postfix}"
            new_thum = img.copy()
            new_thum.thumbnail((width, height))
            new_thum.save(full_path, "WEBP")
            db_value = f'{self.original.name.rsplit('.', 1)[0]}{file_postfix}'
            setattr(self, name, db_value)
            
    class Meta:
        db_table = "thumbnail"
