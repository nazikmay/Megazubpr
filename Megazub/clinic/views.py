from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class CarouselItemViewSets(viewsets.ModelViewSet):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryServiceViewSets(viewsets.ModelViewSet):
    queryset = CategoryService.objects.all()
    serializer_class = CategoryServiceSerializer


class ServiceViewSets(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ActionViewSets(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ServicePhotosViewSets(viewsets.ModelViewSet):
    queryset = ServicePhotos.objects.all()
    serializer_class = ServicePhotosSerializer


class SpecialityDoctorsViewSets(viewsets.ModelViewSet):
    queryset = SpecialityDoctors.objects.all()
    serializer_class = SpecialityDoctorsSerializer


class DoctorsViewSets(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer


class DoctorsSliderViewSets(viewsets.ModelViewSet):
    queryset = DoctorsSlider.objects.all()
    serializer_class = DoctorsSliderSerializer


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ReviewsViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class WorkExampleViewSets(viewsets.ModelViewSet):
    queryset = WorkExample.objects.all()
    serializer_class = WorkExampleSerializer


class QuestionsViewSets(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class VacancyViewSets(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class AppVacanciesViewSets(viewsets.ModelViewSet):
    queryset = AppVacancies.objects.all()
    serializer_class = AppVacanciesSerializer


class IndependentRatingsViewSets(viewsets.ModelViewSet):
    queryset = IndependentRatings.objects.all()
    serializer_class = IndependentRatingsSerializer



class MaterialsClinicViewSets(viewsets.ModelViewSet):
    queryset = MaterialsClinic.objects.all()
    serializer_class = MaterialsClinicSerializer


class ClinicViewSets(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class CertificatesViewSets(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer


class RequisitesViewSets(viewsets.ModelViewSet):
    queryset = Requisites.objects.all()
    serializer_class = RequisitesSerializer


class UsefulInfoViewSets(viewsets.ModelViewSet):
    queryset = UsefulInfo.objects.all()
    serializer_class = UsefulInfoSerializer


class ImageEquipmentViewSets(viewsets.ModelViewSet):
    queryset = ImageEquipment.objects.all()
    serializer_class = ImageEquipmentSerializer


class ImageMaterialsViewSets(viewsets.ModelViewSet):
    queryset = ImageMaterials.objects.all()
    serializer_class = ImageMaterialsSerializer


