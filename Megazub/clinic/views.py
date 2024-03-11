from .models import *
from rest_framework import viewsets
from .serializers import *

class DoctorsListViewSets(viewsets):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsListSerializer


