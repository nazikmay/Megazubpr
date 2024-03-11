from rest_framework import serializers
from .models import *


class DoctorsListSerializer(serializers.ModelSerializer):
    """Список докторов"""

    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsSlider
        fields = '__all__'
