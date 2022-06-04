from django.db import models
from django.urls import reverse


class Video(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    titulos = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    yt_id = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('multi:video', args=(self.slug,))

    def __str__(self):
        return f'Video: {self.titulos}'
