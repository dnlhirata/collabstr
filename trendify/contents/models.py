from django.db import models

from creators.models import Creator


class Content(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'{self.creator.name} - {self.url}'

    @property
    def content_type(self):
        extension = self.url.split('.')[-1]
        match extension:
            case 'jpg' | 'jpeg' | 'png' | 'gif' | 'webp':
                return 'image'
            case 'mp4' | 'webm' | 'avi' | 'mov':
                return 'video'
            case _:
                return 'unknown'