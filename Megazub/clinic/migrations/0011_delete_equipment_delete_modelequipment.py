# Generated by Django 5.0.3 on 2024-03-13 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_modelequipment_equipment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='ModelEquipment',
        ),
    ]