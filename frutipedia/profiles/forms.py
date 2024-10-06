from django import forms

from frutipedia.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ["age", "image_url"]
        labels = {
            "first_name": '',
            "last_name": '',
            "email": '',
            "password": '',
        }

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }


class EditProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ["email", "password",]
