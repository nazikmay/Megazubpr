from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CarouselItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Services(models.Model):
    """Услуги"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    guarantee = models.TextField()
    is_promotion = models.BooleanField(default=False, null=True, blank=True)
    end_promotion = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


"""class ServicePhotos(models.Model):
    image = models.ImageField(upload_to='images/')"""


class SpecialityDoctors(models.Model):
    """Специальность доктора"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Doctors(models.Model):
    """Наши доктора"""
    name = models.CharField("Имя",max_length=100)
    speciality = models.ManyToManyField(SpecialityDoctors, on_delete=models.CASCADE)
    description = models.TextField("Специализация")
    education = models.TextField()
    image = models.ImageField("Фото", upload_to='doctors/')
    year = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.name

class DoctorsSlider(models.Model):
    """Слайдер, "Карусель"""
    title = models.CharField("Название", max_length=100)
    doctors = models.ForeignKey(Doctors, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class News(models.Model):
    """Новости"""
    title = models.CharField(max_length=150)
    descriptions = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    """Отзывы"""
    author = models.CharField(max_length=100)
    text = models.TextField()
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, related_name='reviews', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} for {self.services} by {self.doctors}"


class Questions(models.Model):
    """Остались вопросы? Мы ответим!"""
    name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(max_length=15)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Вакансии"""
    title = models.CharField(max_length=150)
    descriptions = models.TextField()
    salary = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Review by {self.title} - {self.salary} "


class AppVacancies(models.Model):
    """Заявка на вакансию"""
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(max_length=15)
    position = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name


class Works(models.Model):
    """Примеры работ"""
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=256)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='works/')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    time_treatment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title




