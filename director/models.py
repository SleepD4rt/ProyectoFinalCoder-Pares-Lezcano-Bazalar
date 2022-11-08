from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    awards = RichTextField(null=True, blank=True)
    birth = models.DateField()
    films = RichTextField(null=True, blank=True)
 
    def __str__(self):
        return f'Nombre: {self.name} | Apellido: {self.last_name} | Edad: {self.age} | Premios: {self.awards} | Nacimiento: {self.birth}'