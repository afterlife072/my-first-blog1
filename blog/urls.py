from django.urls import path

from mysite.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
