from django import forms
from ckeditor.widgets import CKEditorWidget

from movie.models import Movie

class MovieForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre de la pelicula",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-name",
                "placeholder": "introduzca nombre",
                "required": "True",
            }
        ),
    )
    
    release_date = forms.DateField(
        label="Fecha de estreno",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-release_date",
                "placeholder": "introduzca fecha",
                "required": "True",
            }
        ),
    )
    director = forms.CharField(
        label="Dirigida por",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-director",
                "placeholder": "introduzca nombre",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "movie-description",
                "placeholder": "Descripcion de la pelicula",
                "required": "True",
            }
        ),
    )
    
    image = forms.ImageField()
    
    studio = forms.CharField(
        label="Estudio:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-studio",
                "placeholder": "introduzca nombre",
                "required": "True",
            }
        ),
    )
    
    duration = forms.IntegerField(
        label="Duracion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-duration",
                "placeholder": "introduzca duracion",
                "required": "True",
            }
        ),
    )
    rating = forms.FloatField(
        label="Rating:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-rating",
                "placeholder": "Rating expresado del 0.0 a 10.0",
                "required": "True",
            }
        ),
    )
    
class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )

    class Meta:
        model = Movie
        fields = ["name", "release_date", "director", "description", "image", "studio", "duration", "rating"] 