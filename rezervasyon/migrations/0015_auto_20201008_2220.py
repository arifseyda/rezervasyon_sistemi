# Generated by Django 3.1.1 on 2020-10-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0014_auto_20201008_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(0, 'Power System'), (1, 'Water System'), (2, 'Blade Server')], default=0),
        ),
    ]
