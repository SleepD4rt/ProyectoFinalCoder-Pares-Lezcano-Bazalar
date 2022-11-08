from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from serie.forms import CommentForm
#from serie.forms import serieForm
#from serie.forms import HomeworkForm
from serie.models import Comment
from serie.models import Serie


class serieListView(ListView):
    model = Serie
    paginate_by = 3


class SerieDetailView(DetailView):
    model = Serie
    template_name = "serie/serie_detail.html"
    fields = ["name", "code", "description"]

    def get(self, request, pk):
        serie = Serie.objects.get(id=pk)
        comments = Comment.objects.filter(serie=serie).order_by("-updated_at")
        #comment_form = CommentForm()
        context = {
            "series": serie,
            "comments": comments,
        #    "comment_form": comment_form,
        }
        return render(request, self.template_name, context)

#LoginRequiredMixin
class SerieCreateView(CreateView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")

    form_class = SerieForm
    # fields = ["name", "code", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate series"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Serie.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El curso {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Curso {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)

#LoginRequiredMixin
class SerieUpdateView(UpdateView):
    model = Serie
    fields = ["name", "code", "description", "image"]

    def get_success_url(self):
        serie_id = self.kwargs["pk"]
        return reverse_lazy("serie:serie-detail", kwargs={"pk": serie_id})

#LoginRequiredMixin
class SerieDeleteView(DeleteView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")

#LoginRequiredMixin
class CommentCreateView(CreateView):
    def post(self, request, pk):
        serie = get_object_or_404(serie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, serie=serie
        )
        comment.save()
        return redirect(reverse("serie:serie-detail", kwargs={"pk": pk}))

#LoginRequiredMixin
class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        serie = self.object.serie
        return reverse("serie:serie-detail", kwargs={"pk": serie.id})