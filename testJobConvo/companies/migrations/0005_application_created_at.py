# Generated by Django 5.0.7 on 2024-07-28 14:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_jobposting_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
