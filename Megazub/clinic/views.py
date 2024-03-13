from rest_framework import viewsets
from .serializers import *
from .models import *


class CarouselItemViewSets(viewsets.ModelViewSet):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServiceViewSets(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


"""class ServicePhotosViewSets(viewsets.ModelViewSet):
    queryset = ServicePhotos.objects.all()
    serializer_class = ServicePhotosSerializer
"""


class DoctorsListViewSets(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsListSerializer


class DoctorsSliderViewSets(viewsets.ModelViewSet):
    queryset = DoctorsSlider.objects.all()
    serializer_class = DoctorsSliderSerializer


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ReviewsViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class QuestionsViewSets(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class VacancyViewSets(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class AppVacanciesViewSets(viewsets.ModelViewSet):
    queryset = AppVacancies.objects.all()
    serializer_class = AppVacanciesSerializer


class WorksViewSets(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer


class SpecialityDoctorsViewSets(viewsets.ModelViewSet):
    queryset = SpecialityDoctors.objects.all()
    serializer_class = SpecialityDoctorsSerializer


"""class ModelEquipmentViewSets(viewsets.ModelViewSet):
    queryset = ModelEquipment.objects.all()
    serializer_class = ModelEquipmentSerializer


class EquipmentViewSets(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
"""

