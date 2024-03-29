# Generated by Django 5.0.3 on 2024-03-13 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_doctors_certificates_alter_doctors_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='IndependentRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=44)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], help_text='Оцените сайт от 1 до 10.', verbose_name='Rating')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialsClinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Requisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=64)),
                ('legal_address', models.TextField()),
                ('email_address', models.TextField()),
                ('inn', models.IntegerField()),
                ('kpp', models.IntegerField()),
                ('bik', models.IntegerField()),
                ('p_c', models.TextField()),
                ('k_c', models.IntegerField()),
                ('okpo', models.IntegerField()),
                ('okato', models.IntegerField()),
                ('okved', models.FloatField()),
                ('odrn', models.IntegerField()),
                ('general_manager', models.CharField(max_length=44)),
                ('electronic_email', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveIntegerField()),
                ('site_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicePhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='services',
        ),
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AddField(
            model_name='reviews',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='reviews',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.services'),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='image',
            field=models.ImageField(null=True, upload_to='doctors/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='speciality',
            field=models.ManyToManyField(related_name='speciality_doctor', to='clinic.specialitydoctors'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='author',
            field=models.CharField(max_length=44),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='doctors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.doctors'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='parent_review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='clinic.reviews'),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=74)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('end_date', models.DateField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('services', models.ManyToManyField(related_name='actions', to='clinic.services')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.category')),
            ],
        ),
        migrations.AddField(
            model_name='services',
            name='category_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.categoryservice'),
        ),
        migrations.CreateModel(
            name='UsefulInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('category_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.categoryservice')),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('srok_lechenie', models.IntegerField()),
                ('history_client', models.TextField()),
                ('category_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.categoryservice')),
                ('doctors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.doctors')),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.reviews')),
            ],
        ),
        migrations.DeleteModel(
            name='Works',
        ),
    ]
