from django.db import models

class Doctors(models.Model):
    """Наши доктора"""
    name = models.CharField("Имя",max_length=100)
    description = models.TextField("Специализация")
    image = models.ImageField("Фото", upload_to='doctors/')
    year = models.PositiveSmallIntegerField("Опыт работы", default=0)
    #review = models.ForeignKey("Отзывы", Reviews,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DoctorsSlider(models.Model):
    """Слайдер, "Карусель"""
    title = models.CharField("Название", max_length=100)
    doctors = models.ForeignKey(Doctors, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


