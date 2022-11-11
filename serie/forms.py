from ckeditor.widgets import CKEditorWidget
from django import forms

from serie.models import Serie


class SerieForm(forms.ModelForm):

    name = forms.CharField(
        label="Nombre de la serie",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-name",
                "placeholder": "Nombre de la serie",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    chapter = forms.IntegerField(
        label="Capitulos:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-chapter",
                "placeholder": "Cantidad de capitulos",
                "required": "True",
            }
        ),
    )

    season = forms.IntegerField(
        label="Temporadas:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-season",
                "placeholder": "Cantidad de temporadas",
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

    director = forms.CharField(
        label="Nombre y apellido del director",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-director",
                "placeholder": "Director",
                "required": "True",
            }
        ),
    )

    actor = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    studio = forms.CharField(
        label="Nombre del estudio",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-studio",
                "placeholder": "Estudio",
                "required": "True",
            }
        ),
    )

    release_date = forms.DateField(
        label="Fecha de estreno:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-realease_date",
                "placeholder": "Fecha yyyy-mm-dd",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Serie
        fields = ["name", "descript", "chapter", "season", "rating", "director", "actor", "studio", "release_date"]


  

  


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

