from django.db import models
from django.forms import ModelForm
from django.utils.text import slugify
from django.urls import reverse

class Ytdl(models.Model):
    l_ytdl_url = models.URLField(max_length=200, verbose_name="Video URL")
    l_ytdl_title = models.CharField(max_length=200, verbose_name="Title")

    slug = models.SlugField(null=False, unique=False, default=None) 

    class Meta:
        ordering = ["l_ytdl_title"]

    def __str__(self):
        return self.l_ytdl_title

    def get_absolute_url(self):
        return reverse('ytdl:index')

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.l_ytdl_title)
        return super().save(*args, **kwargs)


class YtdlModelForm(ModelForm):
    class Meta:
        model = Ytdl
        fields = ['l_ytdl_url']