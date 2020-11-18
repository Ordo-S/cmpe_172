from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Ytdl, YtdlModelForm
from django.views.generic.edit import CreateView
from django.views import generic

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


    yt.streams.first().download()
    
    instance = Ytdl.objects.create(l_ytdl_title=title, l_ytdl_url=video_url)
    instance.save()
    #res = render(request, "download/")

    return redirect('ytdl:index')