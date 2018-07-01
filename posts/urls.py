from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.post_list),
    re_path(r'^create/$', views.post_create),
    re_path(r'^detail/$', views.post_detail),
    re_path(r'^update/$', views.post_update),
    re_path(r'^delete/$', views.post_delete),
]
