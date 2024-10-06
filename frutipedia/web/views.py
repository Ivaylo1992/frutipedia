from django.shortcuts import render
from django.views import generic as views

from frutipedia.core.view_mixins import HasProfileMixin
from frutipedia.fruit.models import Fruit


class IndexView(HasProfileMixin, views.TemplateView):
    template_name = 'web/index.html'


class DashboardView(HasProfileMixin, views.ListView):
    queryset = Fruit.objects.all()
    template_name = "web/dashboard.html"
