# Generated by Django 3.1.1 on 2020-09-22 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0009_reservation_deneme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='deneme',
        ),
    ]
