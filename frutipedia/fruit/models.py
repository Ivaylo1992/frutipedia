from django.core.validators import MinLengthValidator
from django.db import models

from frutipedia.fruit.validators import validate_fruit_name
from frutipedia.profiles.models import Profile


class Fruit(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    UNIQUE_FRUIT_NAME_MESSAGE = "This fruit name is already in use! Try a new one."

    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_fruit_name,
        ],
        error_messages={
            'unique': UNIQUE_FRUIT_NAME_MESSAGE,
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )