from django.db import models


# Create your models here.

class Movie(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
        ('CHINESE', 'Chinese'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
    )
    rating_choice = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG13', 'PG13'),
        ('NC16', 'NC16'),
        ('M18', 'M18'),
        ('R21', 'R21')
    )
    name = models.CharField(max_length=20)
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=20)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes")
    certificate = models.CharField(max_length=4, choices=rating_choice)
    popularity_index = models.IntegerField(unique=True, null=True, blank=True)
    trailer = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.name
