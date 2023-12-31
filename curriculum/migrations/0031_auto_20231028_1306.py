# Generated by Django 3.2.6 on 2023-10-28 18:06

import curriculum.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0030_auto_20210511_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='Notes',
            field=models.FileField(blank=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Anotaciones'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nombre del capitulo'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='position',
            field=models.PositiveSmallIntegerField(verbose_name='Numero del capitulo'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='ppt',
            field=models.FileField(blank=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Pdf'),
        ),
    ]
