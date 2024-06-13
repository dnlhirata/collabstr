from django.db import models

from creators.models import Creator


class Content(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'{self.creator.name} - {self.url}'