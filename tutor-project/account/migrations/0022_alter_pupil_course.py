# Generated by Django 4.1.4 on 2023-01-16 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_alter_pupil_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.cours'),
        ),
    ]
