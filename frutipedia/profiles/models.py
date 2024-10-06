from django.core.validators import MinLengthValidator
from django.db import models

from frutipedia.profiles.validators import validate_name


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 35
    LAST_NAME_MIN_LENGTH = 1
    EMAIL_MAX_LENGTH = 40
    PASSWORD_MAX_LENGTH = 20
    PASSWORD_MIN_LENGTH = 8
    HELPTEXT_PASSWORD = "*Password length requirements: 8 to 20 characters"
    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_name,
        ],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_name,
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=EMAIL_MAX_LENGTH,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LENGTH,
        validators=[
            MinLengthValidator(PASSWORD_MIN_LENGTH),
        ],
        help_text=HELPTEXT_PASSWORD,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default = DEFAULT_AGE
    )

    @property
    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        return f"Noname{self.pk}"