from django.db import models


class CarouselItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    description = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Категория Услуг 1"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CategoryService(models.Model):
    """Категория Услуг 2"""
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Services(models.Model):
    """Услуга"""
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=70)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    guarantee = models.TextField()
    is_promotion = models.BooleanField(default=False, null=True, blank=True)
    end_promotion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Action(models.Model):
    """Акция"""
    title = models.CharField(max_length=74)
    services = models.ManyToManyField(Services, related_name='actions')
    price = models.IntegerField()
    description = models.TextField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True)


class ServicePhotos(models.Model):
    """Картинки для Услуг"""
    image = models.ImageField(upload_to='images/', null=True)


class SpecialityDoctors(models.Model):
    """Специальность доктора"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Doctors(models.Model):
    """Наши доктора"""
    name = models.CharField("Имя", max_length=100)
    speciality = models.ManyToManyField(SpecialityDoctors, related_name='speciality_doctor')
    description = models.TextField()
    education = models.TextField()
    certificates = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField("Фото", upload_to='doctors/', null=True)
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
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    """Отзывы"""
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=44)
    text = models.TextField()
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"Review by {self.author} for {self.service} by {self.doctors}"


class WorkExample(models.Model):
    """Примеры Работы"""
    image = models.ImageField(null=True)
    title = models.CharField(max_length=100)
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE, null=True, blank=True)
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True, blank=True)
    srok_lechenie = models.IntegerField()
    history_client = models.TextField()
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)


class Questions(models.Model):
    """Остались вопросы? Мы ответим!"""
    name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()

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
    """Заявка на вакансию, POST"""
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    position = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name


class IndependentRatings(models.Model):
    """Независимые рейтинги"""
    title = models.CharField(max_length=44)
    image = models.ImageField(null=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], help_text="Оцените сайт от 1 до 10.",
                                verbose_name="Rating")


class MaterialsClinic(models.Model):
    """Материалы Клиники"""
    title = models.CharField(max_length=100)
    description = models.TextField()


class ImageMaterials(models.Model):
    materials_clinic = models.ForeignKey(MaterialsClinic, on_delete=models.CASCADE)
    image = models.ImageField()


class Clinic(models.Model):
    """Клиника"""
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(null=True)


class Equipment(models.Model):
    """Работаем на профессиональном оборудовании"""
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=60)


class ImageEquipment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    image = models.ImageField()


class Certificates(models.Model):
    """Сертификаты"""
    image = models.ImageField(null=True)
    description = models.TextField()


class Requisites(models.Model):
    """Реквизиты"""
    name_organization = models.CharField(max_length=64)
    legal_address = models.TextField()
    email_address = models.TextField()
    inn = models.IntegerField()
    kpp = models.IntegerField()
    bik = models.IntegerField()
    p_c = models.TextField()
    k_c = models.IntegerField()
    okpo = models.IntegerField()
    okato = models.IntegerField()
    okved = models.FloatField()
    odrn = models.IntegerField()
    general_manager = models.CharField(max_length=44)
    electronic_email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    site_url = models.URLField()


class UsefulInfo(models.Model):
    """Полезная Информация"""
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE)


