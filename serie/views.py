from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from serie.forms import CommentForm
from serie.forms import SerieForm
#from serie.models import Comment
from serie.models import Serie


class serieListView(ListView):
    model = Serie
    paginate_by = 2


class SerieDetailView(DetailView):
    model = Serie
    template_name = "serie/serie_detail.html"
    fields = ["name", "description", "release_date", "chapter", "season", "rating", "image", "director", "actor", "studio"]

#LoginRequiredMixin
class SerieCreateView(LoginRequiredMixin, CreateView):
    model = Serie

    success_url = reverse_lazy("serie:serie-list")
    
    form_class = SerieForm

    def form_valid(self, form):
        """Filter to avoid duplicate series"""
        data = form.cleaned_data
        actual_objects = Serie.objects.filter(
            name=data["name"], 
            studio=data["studio"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La serie {data['name']}, producida por {data['studio']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"La serie {data['name']} - {data['studio']} creado exitosamente!",
            )
            return super().form_valid(form)

#LoginRequiredMixin
class SerieUpdateView(LoginRequiredMixin, UpdateView):
    model = Serie
    fields = ["name", "description", "release_date", "chapter", "season", "rating", "image", "director", "actor", "studio"]

    def get_success_url(self):
        serie_id = self.kwargs["pk"]
        return reverse_lazy("serie:serie-detail", kwargs={"pk": serie_id})

#LoginRequiredMixin
class SerieDeleteView(LoginRequiredMixin, DeleteView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")
    
    
    #Buscador
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        series = Serie.objects.filter(query)
        context_dict.update(
            {
                "series": series,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="serie/serie_search.html",
    )
    

"""

class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        serie = get_object_or_404(serie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, serie=serie
        )
        comment.save()
        return redirect(reverse("serie:serie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        serie = self.object.serie
        return reverse("serie:serie-detail", kwargs={"pk": serie.id})
"""