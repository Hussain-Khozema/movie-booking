# Generated by Django 3.2.6 on 2021-08-31 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be of 8 digits', regex='^[8-9]\\d{7}$')]),
        ),
    ]
