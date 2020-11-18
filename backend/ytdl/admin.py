from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Ytdl


class YtdlAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['l_ytdl_title']}),
        ('Video Url',               {'fields': ['l_ytdl_url']}),
        ('Slug', {'fields': ['slug']})
    ]

    prepopulated_fields = {'slug': ('l_ytdl_title',)}
    search_fields = ('l_ytdl_title', 'l_ytdl_title' )
    


admin.site.register(Ytdl, YtdlAdmin)
   