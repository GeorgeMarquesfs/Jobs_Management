# Generated by Django 5.0.7 on 2024-07-28 12:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_rename_education_level_application_highest_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
