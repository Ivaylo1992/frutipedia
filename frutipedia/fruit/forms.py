from django import forms

from frutipedia.fruit.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        exclude = ("owner",)


class CreateFruitForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Fruit Name"}),
            "description": forms.Textarea(attrs={"placeholder": "Fruit Description"}),
            "image_url": forms.URLInput(attrs={"placeholder": "Fruit Image URL"}),
            "nutrition": forms.Textarea(attrs={"placeholder": "Nutritional Info"}),
        }

        labels = {
            "name": "",
            "description": "",
            "image_url": "",
            "nutrition": "",
        }


class EditFruitForm(FruitBaseForm):
    ...


class DeleteFruitForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        exclude = ("owner", "description",)

    def __init__(self, *args, **kwargs):
        super(DeleteFruitForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['readonly'] = "readonly"

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance