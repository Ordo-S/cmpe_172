from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Ytdl, YtdlModelForm
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.static import serve
import os
from wsgiref.util import FileWrapper

from pytube import YouTube

class IndexView(generic.ListView):
    template_name = 'ytdl/index.html'
    context_object_name = 'ytdlList'

    def get_queryset(self):
        return Ytdl.objects.order_by('l_ytdl_title')

class DetailView(generic.DetailView):
    model = Ytdl      
    template_name = "ytdl/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['videoList'] = Ytdl.objects.all()
        return context


class IndexViewCreate(CreateView):
    template_name = 'ytdl/ytdl_create.html'
    form_class = YtdlModelForm
    queryset = Ytdl.objects.all()
    

def download(request):
    print ("Yeeeet")
   
    video_url = request.POST.get("l_ytdl_url", False)
    yt = YouTube(video_url)

    thumbnail_url = yt.thumbnail_url
    title = yt.title
    length = yt.length
    desc = yt.description
    rating = yt.rating
    dirs = './Downloads'

    # Hit that model with the good stuff 
    instance = Ytdl.objects.create(l_ytdl_title=title, l_ytdl_url=video_url)
    instance.save()
    
    # Download Stuff
    pls = yt.streams.first().download(dirs)
    wrapper = FileWrapper(open(pls, 'rb'))
    response = HttpResponse(wrapper, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=CMPE_Vid.mp4'

    # Clean up Downloads
    downloads = os.listdir("./Downloads")
    print(downloads)
    for vid in downloads:
        if vid.endswith(".mp4"):
            os.remove(os.path.join(dirs, vid))
    
    return response
    