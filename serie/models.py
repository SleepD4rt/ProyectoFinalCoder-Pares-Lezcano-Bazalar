from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField


class Serie(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    descript = RichTextField(null=True, blank=True)
    chapter = models.IntegerField(null=False, blank=False)
    season = models.IntegerField(null=False, blank=False)
    rating = models.FloatField(null=False, blank=False)
    image = models.ImageField(upload_to='serie', null=True, blank=True)
    director = models.CharField(max_length=40, null=False, blank=False)
    actor = RichTextField(null=True, blank=True)
    studio = models.CharField(max_length=40, null=False, blank=False)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    launch_day =models.DateField(null=False, blank=False)
    publish_at = models.DateTimeField(auto_now_add=True)

"""
    class Meta:
        unique_together = (
            "name",
            "studio",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Course: {self.name} | code: {self.code}"
"""

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

