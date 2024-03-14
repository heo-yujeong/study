# Generated by Django 4.2.11 on 2024-03-14 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_apiinfo_additional_info_alter_apiinfo_api_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='api_url',
            field=models.URLField(validators=[django.core.validators.URLValidator(60), django.core.validators.MinLengthValidator(15)]),
        ),
    ]
