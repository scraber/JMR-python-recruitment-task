from django.core.validators import RegexValidator
from django.db import models


class Url(models.Model):
    full_url = models.URLField()
    code = models.CharField(
        max_length=255,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[-a-zA-Z0-9_]+$",
                message="Code can only contain hyphens, lowercase/uppercase letters, numbers and underscores",
            )
        ],
    )

    def __str__(self) -> str:
        return f"{self.full_url} -> Shorty: {self.code}"
