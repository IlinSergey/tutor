# Generated by Django 4.1.4 on 2023-01-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_cours_author_alter_pupil_age_alter_pupil_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='lenght',
            field=models.IntegerField(verbose_name='Продолжительность курса, часов'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Возраст'),
        ),
    ]
