from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('i.html', views.i, name="i")
]