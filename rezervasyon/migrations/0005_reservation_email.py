# Generated by Django 3.1.1 on 2020-09-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0004_auto_20200916_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
