from rest_framework import serializers
from .models import *


class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'


"""class ServicePhotosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePhotos
        fields = '__all__'
"""

class DoctorsListSerializer(serializers.ModelSerializer):
    """Список докторов"""

    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsSlider
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
