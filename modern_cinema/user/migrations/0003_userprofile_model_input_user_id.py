# Generated by Django 3.2.6 on 2021-09-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='model_input_user_id',
            field=models.CharField(default='Default', max_length=20),
            preserve_default=False,
        ),
    ]
