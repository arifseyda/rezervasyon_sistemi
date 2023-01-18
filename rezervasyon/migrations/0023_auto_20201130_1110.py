# Generated by Django 3.0.3 on 2020-11-30 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0022_auto_20201009_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status2',
            field=models.SmallIntegerField(choices=[(0, 'Evet'), (1, 'Hayır')], default=1, verbose_name='Kontrol Paneli'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='E-mail Adresiniz'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, verbose_name='Soyadınız'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserved_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Bitiş Zamanı'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserved_start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserved_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Başlangıç Zamanı'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Power System'), (1, 'Water System'), (2, 'Blade')], default=0, verbose_name='Seçenekler'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='username',
            field=models.CharField(blank=True, max_length=20, verbose_name='Adınız'),
        ),
    ]
