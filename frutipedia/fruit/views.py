from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from frutipedia.core.view_mixins import HasProfileMixin, get_profile
from frutipedia.fruit.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from frutipedia.fruit.models import Fruit


class CreateFruitView(HasProfileMixin, views.CreateView):
    model = Fruit
    template_name = "fruit/create-fruit.html"
    form_class = CreateFruitForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)


class DetailsFruitView(HasProfileMixin, views.DetailView):
    model = Fruit
    template_name = "fruit/details-fruit.html"
    pk_url_kwarg = "fruitId"


class EditFruitView(HasProfileMixin, views.UpdateView):
    model = Fruit
    template_name = "fruit/edit-fruit.html"
    form_class = EditFruitForm
    success_url = reverse_lazy("dashboard")

    pk_url_kwarg = "fruitId"


class DeleteFruitView(HasProfileMixin, views.DeleteView):
    model = Fruit
    template_name = "fruit/delete-fruit.html"
    success_url = reverse_lazy("dashboard")
    form_class = DeleteFruitForm

    pk_url_kwarg = "fruitId"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

