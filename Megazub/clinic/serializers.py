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


class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class ServicePhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePhotos
        fields = '__all__'


class SpecialityDoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityDoctors
        fields = '__all__'


class DoctorsSerializer(serializers.ModelSerializer):
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


class WorkExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExample
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class AppVacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVacancies
        fields = '__all__'


class IndependentRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndependentRatings
        fields = '__all__'


class MaterialsClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialsClinic
        fields = '__all__'


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'


class RequisitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisites
        fields = '__all__'


class UsefulInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulInfo
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class ImageEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEquipment
        fields = '__all__'


class ImageMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMaterials
        fields = '__all__'

"""
class ModelEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelEquipment
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
"""