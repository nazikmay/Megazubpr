from rest_framework import viewsets
from .serializers import DoctorsListSerializer, DoctorsSliderSerializer
from .models import Doctors, DoctorsSlider

class DoctorsListViewSets(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsListSerializer

class DoctorsSliderViewSets(viewsets.ModelViewSet):
    queryset = DoctorsSlider.objects.all()
    serializer_class = DoctorsSliderSerializer
