# video/urls.py
from django.conf.urls import url, include
from board import views
from django.urls import path

app_name = "board"

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),

#    url(r'^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
#    path('$', views.video_list, name='list')
]
