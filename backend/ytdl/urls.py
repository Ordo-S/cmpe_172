from django.urls import path
from . import views


app_name = 'ytdl'

urlpatterns = [
    path('ytdl', views.IndexView.as_view(), name='index'),
    path('create', views.IndexViewCreate.as_view(), name="create-link"),
    path('download/', views.download, name="download"),
    path('ytdl/<int:pk>/', views.DetailView.as_view(), name='detail')
]