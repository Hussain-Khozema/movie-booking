# Generated by Django 3.2.6 on 2021-09-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('ENGLISH', 'English'), ('CHINESE', 'Chinese'), ('HINDI', 'Hindi'), ('TAMIL', 'Tamil')], max_length=10),
        ),
    ]