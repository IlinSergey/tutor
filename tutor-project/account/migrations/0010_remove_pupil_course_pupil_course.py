# Generated by Django 4.1.4 on 2023-01-14 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_pupil_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='course',
        ),
        migrations.AddField(
            model_name='pupil',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.cours'),
        ),
    ]