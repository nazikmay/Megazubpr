from django.urls import path, include, re_path
from .views import *




urlpatterns = [


    path('doctors/', DoctorsListViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='doctors_list'),
    path('doctors/<int:pk>/', DoctorsListViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='doctors_detail'),
    path('slider/', DoctorsSliderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='slider_list'),
    path('slider/<int:pk>/', DoctorsSliderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='carousel_detail'),
    ]