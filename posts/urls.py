from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='list'),
    re_path(r'^create/$', views.post_create),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete),
    re_path(r'^about$', views.about),
]
