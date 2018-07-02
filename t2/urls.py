from django.urls import path
from . import views

urlpatterns = [
    
    path('1/', views.one, name='one'),
    path('2/', views.two, name='two'),
    path('3/', views.three, name='three'),
    path('4/', views.four, name='four'),
    path('5/', views.five, name='five'),  
    path('', views.index, name='index'),
]