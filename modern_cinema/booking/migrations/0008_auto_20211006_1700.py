# Generated by Django 3.2.6 on 2021-10-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_bookedseat_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('id', 'show')},
        ),
    ]