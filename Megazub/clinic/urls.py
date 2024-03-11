from django.urls import path, include, re_path
from .views import *


urlpatterns = [


    path('carousel/', CarouselItemViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='carousel_list'),
    path('carousel/<int:pk>/', CarouselItemViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='carousel_detail'),

    path('categories/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('categories/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('service/', ServiceViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='service_list'),
    path('service/<int:pk>/', ServiceViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='service_detail'),


#   path('service_photos/', ServicePhotosViewSets.as_view({'get': 'list', 'post': 'create'}),
 #        name='service_photos_list'),
  #  path('service_photos/<int:pk>/', ServicePhotosViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
   #      name='service_photos_detail'),


    path('doctors/', DoctorsListViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='doctors_list'),
    path('doctors/<int:pk>/', DoctorsListViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='doctors_detail'),
    path('slider/', DoctorsSliderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='slider_list'),
    path('slider/<int:pk>/', DoctorsSliderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='slider_detail'),
    path('news/', NewsViewSets.as_view({'get': 'list', 'post': 'create'}), name='new_list'),
    path('news/<int:pk>/', NewsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='new_detail'),
    path('reviews/', ReviewsViewSets.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('reviews/<int:pk>/', ReviewsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),

]