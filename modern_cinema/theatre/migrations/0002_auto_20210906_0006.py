# Generated by Django 3.2.6 on 2021-09-05 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='theatre',
        ),
        migrations.DeleteModel(
            name='Theatre',
        ),
    ]