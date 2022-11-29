from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
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
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = (
            "name",
            "studio",
        )
    ordering = ["-realease_date"]


    def __str__(self):
        return f"Name: {self.name} - Release_date: {self.release_date} - Produced_by: {self.director}  "
        

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
