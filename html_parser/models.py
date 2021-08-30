from django.db import models


class Url(models.Model):
    """Url storage model"""
    id = models.AutoField(primary_key=True)
    url = models.URLField()

    class Meta:
        ordering = ['-id']
