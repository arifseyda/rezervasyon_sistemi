# Generated by Django 3.1.1 on 2020-09-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0008_auto_20200918_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='deneme',
            field=models.IntegerField(default=0),
        ),
    ]
