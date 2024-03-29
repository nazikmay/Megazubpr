from django.urls import path, include, re_path
from .views import *


urlpatterns = [

    path('carousel_item/', CarouselItemViewSets.as_view({'get': 'list'}),
         name='carousel_item_list'),
    path('carousel_item/<int:pk>/',
         CarouselItemViewSets.as_view({'get': 'retrieve'}),
         name='carousel_item_detail'),
    path('category/', CategoryViewSets.as_view({'get': 'list'}),
         name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve'}),
         name='category_detail'),
    path('category_service/', CategoryServiceViewSets.as_view({'get': 'list'}),
         name='category_service_list'),
    path('category_service/<int:pk>/',
         CategoryServiceViewSets.as_view({'get': 'retrieve'}),
         name='category_service_detail'),
    path('service/', ServiceViewSets.as_view({'get': 'list'}),
         name='service_list'),
    path('service/<int:pk>/', ServiceViewSets.as_view({'get': 'retrieve'}),
         name='service_detail'),
    path('action/', ActionViewSets.as_view({'get': 'list'}),
         name='action_list'),
    path('action/<int:pk>/', ActionViewSets.as_view({'get': 'retrieve'}),
         name='action_detail'),
    path('service_photos/', ServicePhotosViewSets.as_view({'get': 'list'}),
         name='service_photos_list'),
    path('service_photos/<int:pk>/',
         ServicePhotosViewSets.as_view({'get': 'retrieve'}),
         name='service_photos_detail'),
    path('speciality_doctors/', SpecialityDoctorsViewSets.as_view({'get': 'list'}),
         name='speciality_doctors_list'),
    path('speciality_doctors/<int:pk>/',
         SpecialityDoctorsViewSets.as_view({'get': 'retrieve'}),
         name='speciality_doctors_detail'),
    path('doctors/', DoctorsViewSets.as_view({'get': 'list'}),
         name='doctors_list'),
    path('doctors/<int:pk>/', DoctorsViewSets.as_view({'get': 'retrieve'}),
         name='doctors_detail'),
    path('doctors_slider/', DoctorsSliderViewSets.as_view({'get': 'list'}),
         name='doctors_slider_list'),
    path('doctors_slider/<int:pk>/',
         DoctorsSliderViewSets.as_view({'get': 'retrieve'}),
         name='doctors_slider_detail'),
    path('news/', NewsViewSets.as_view({'get': 'list'}),
         name='news_list'),
    path('news/<int:pk>/', NewsViewSets.as_view({'get': 'retrieve'}),
         name='news_detail'),
    path('reviews/', ReviewsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='reviews_list'),
    path('reviews/<int:pk>/', ReviewsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reviews_detail'),
    path('work_example/', WorkExampleViewSets.as_view({'get': 'list'}),
         name='work_example_list'),
    path('work_example/<int:pk>/',
         WorkExampleViewSets.as_view({'get': 'retrieve'}),
         name='work_example_detail'),
    path('questions/', QuestionsViewSets.as_view({'get': 'list'}),
         name='questions_list'),
    path('questions/<int:pk>/', QuestionsViewSets.as_view({'get': 'retrieve'}),
         name='questions_detail'),
    path('vacancy/', VacancyViewSets.as_view({'get': 'list'}),
         name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyViewSets.as_view({'get': 'retrieve'}),
         name='vacancy_detail'),
    path('app_vacancies/', AppVacanciesViewSets.as_view({'get': 'list', 'post': 'add'}),
         name='app_vacancies_list'),
    path('app_vacancies/<int:pk>/',
         AppVacanciesViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='app_vacancies_detail'),
    path('independent_ratings/', IndependentRatingsViewSets.as_view({'get': 'list'}),
         name='independent_ratings_list'),
    path('independent_ratings/<int:pk>/',
         IndependentRatingsViewSets.as_view({'get': 'retrieve'}),
         name='independent_ratings_detail'),
    path('materials_clinic/', MaterialsClinicViewSets.as_view({'get': 'list'}),
         name='materials_clinic_list'),
    path('materials_clinic/<int:pk>/',
         MaterialsClinicViewSets.as_view({'get': 'retrieve'}),
         name='materials_clinic_detail'),
    path('clinic/', ClinicViewSets.as_view({'get': 'list'}),
         name='clinic_list'),
    path('clinic/<int:pk>/', ClinicViewSets.as_view({'get': 'retrieve'}),
         name='clinic_detail'),
    path('certificates/', CertificatesViewSets.as_view({'get': 'list'}),
         name='certificates_list'),
    path('certificates/<int:pk>/',
         CertificatesViewSets.as_view({'get': 'retrieve'}),
         name='certificates_detail'),
    path('requisites/', RequisitesViewSets.as_view({'get': 'list'}),
         name='requisites_list'),
    path('requisites/<int:pk>/', RequisitesViewSets.as_view({'get': 'retrieve'}),
         name='requisites_detail'),
    path('useful_info/', UsefulInfoViewSets.as_view({'get': 'list'}),
         name='useful_info_list'),
    path('useful_info/<int:pk>/', UsefulInfoViewSets.as_view({'get': 'retrieve'}),
         name='useful_info_detail'),
    path('equipment/', EquipmentViewSets.as_view({'get': 'list'}),
         name='equipment_list'),
    path('equipment/<int:pk>/', EquipmentViewSets.as_view({'get': 'retrieve'}),
         name='equipment_detail'),
    path('image_equipment/', ImageEquipmentViewSets.as_view({'get': 'list'}),
         name='image_equipment_list'),
    path('image_equipment/<int:pk>/', ImageEquipmentViewSets.as_view({'get': 'retrieve'}),
         name='image_equipment_detail'),
    path('image_materials/', ImageMaterialsViewSets.as_view({'get': 'list'}),
         name='image_materials_list'),
    path('image_materials/<int:pk>/', ImageMaterialsViewSets.as_view({'get': 'retrieve'}),
         name='image_materials_detail'),

]
