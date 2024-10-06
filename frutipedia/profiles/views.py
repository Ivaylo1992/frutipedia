from django.shortcuts import render
from django.urls import reverse_lazy

from frutipedia.core.view_mixins import get_profile, HasProfileMixin, GetProfileObjectMixin
from frutipedia.profiles.forms import CreateProfileForm, EditProfileForm
from frutipedia.profiles.models import Profile
from django.views import generic as views


class CreateProfileView(HasProfileMixin, views.CreateView):
    model = Profile
    template_name = "profiles/create-profile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy("dashboard")


class DetailsProfileView(GetProfileObjectMixin, HasProfileMixin, views.DetailView):
    model = Profile
    template_name = "profiles/details-profile.html"


class EditProfileView(GetProfileObjectMixin, HasProfileMixin, views.UpdateView):
    model = Profile
    template_name = "profiles/edit-profile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("dashboard")


class DeleteProfileView(GetProfileObjectMixin, HasProfileMixin, views.DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")
