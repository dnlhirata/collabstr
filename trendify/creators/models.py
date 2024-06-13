from django.db import models


class Creator(models.Model):
    class Platform(models.TextChoices):
        INSTAGRAM = 'IG', 'Instagram'
        TIKTOK = 'TK', 'TikTok'
        USER_GENERATED = 'UG', 'User Generated'

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    rating = models.FloatField()
    platform = models.CharField(max_length=255, choices=Platform, default=Platform.USER_GENERATED)

    def __str__(self):
        return self.name