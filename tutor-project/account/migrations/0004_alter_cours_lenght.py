# Generated by Django 4.1.4 on 2023-01-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_cours_lenght'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='lenght',
            field=models.IntegerField(null=True, verbose_name='Продолжительность курса'),
        ),
    ]