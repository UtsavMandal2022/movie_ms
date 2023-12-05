from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=100,blank=True,null=True)
    movie_year = models.IntegerField(blank=True,null=True)
    movie_rating = models.FloatField(blank=True,null=True)
    movie_release_date = models.DateField(blank=True,null=True)
    movie_language = models.CharField(max_length=100,blank=True,null=True)
    movie_cast = models.CharField(max_length=10000,blank=True,null=True)
    movie_director = models.CharField(max_length=100,blank=True,null=True)
    movie_runtime = models.IntegerField(blank=True,null=True)
    movie_description = models.CharField(max_length=1000,blank=True,null=True)
    # movie_poster = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.movie_name