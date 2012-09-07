from django.db import models
from django.contrib.auth.models import User

class Demography(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __unicode__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __unicode__(self):
        return self.name  
    
class Anime(models.Model):
    title = models.CharField(max_length=60)
    original_title = models.CharField(max_length=60)
    poster = models.ImageField(upload_to='images/')
    demography = models.ForeignKey(Demography)
    genres = models.ManyToManyField(Genre)
    synopsis = models.TextField()
    page = models.URLField()
    related = models.ManyToManyField('self')
    rated =  models.BooleanField()
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __unicode__(self):
        return self.title
    
#    class Meta:
#        abstract = True
        
class Episode(models.Model):
    title = models.CharField(max_length=50)
    number = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    
    def __unicode__(self):
        return self.title
            
class Show(Anime):
    STATUS_CHOICES = (
        ('finished', 'Finalizada'),
        ('onair', 'En transmision'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    number_of_episodes = models.IntegerField()
    episodes = models.ManyToManyField(Episode)
    started_date = models.DateField()
    finished_date = models.DateField()
    
class Movie(Anime):
    premiere_date = models.DateField()
    
class LiveAction(Anime):
    premiere_date = models.DateField()

class Ova(Anime):
    relase_date = models.DateField()
    episodes = models.ManyToManyField(Episode)    
    
class Bagde(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __unicode__(self):
        return self.name

class CheckIn(models.Model):
    anime = models.ForeignKey(Anime)
    points = models.IntegerField()
    comment = models.CharField(max_length=100)  
      
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=50)
    chekins = models.ManyToManyField(CheckIn)
    bagdes = models.ManyToManyField(Bagde)
    points = models.IntegerField()      

class Review(models.Model):
    title = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    coment = models.TextField()
    anime = models.ForeignKey(Anime)
    user = models.ForeignKey(User)
    date = models.DateField()