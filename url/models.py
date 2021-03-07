from django.db import models


class Url(models.Model):
    full_url = models.URLField()
    code = models.CharField(
        max_length=255,
    )

    def __str__(self) -> str:
        return f"{self.full_url} -> Shorty: {self.code}"