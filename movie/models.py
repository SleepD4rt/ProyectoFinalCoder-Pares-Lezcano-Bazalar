from django.db import models
from ckeditor.fields import RichTextField


class Movie(models.Model):
    name = models.CharField(max_length=40)
    release_date = models.DateField(null=False, blank=False)
    director = models.CharField(max_length=20)
    duration = models.IntegerField(null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    studio = models.CharField(max_length=20)
    image = models.ImageField(upload_to='movie', null=True, blank=True)
    rating = models.FloatField(null=False, blank=False)

    class Meta:
        unique_together = (
            "name",
            "studio",
        )
    ordering = ["-realease_date"]


    def __str__(self):
        return f"Name: {self.name} - Release_date: {self.release_date} - Produced_by: {self.director}  "
        