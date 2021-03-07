from django.db import models


class Url(models.Model):
    full_url = models.URLField()
    hash_url = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"URL: {self.full_url} -> Shorty: {self.hash_url}"