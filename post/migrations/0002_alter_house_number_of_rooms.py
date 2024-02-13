# Generated by Django 5.0.2 on 2024-02-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='number_of_rooms',
            field=models.CharField(choices=[('1 ROOM', '1 КОМНАТА'), ('2 ROOMS', '2 КОМНАТЫ'), ('3 ROOMS', '3 КОМНАТЫ'), ('4 ROOMS', '4 КОМНАТЫ'), ('5 ROOMS', '5 КОМНАТЫ'), ('6 ROOMS', '6 КОМНАТЫ'), ('7 ROOMS', '7 КОМНАТЫ')], max_length=100, verbose_name='Количество комнат'),
        ),
    ]