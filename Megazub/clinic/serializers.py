from rest_framework import serializers
from .models import *

class DoctorsListSerializer(serializers.ModelSerializer):
    """Список докторов"""

    class Meta:
        model = Doctors
        fields = '__all__'
