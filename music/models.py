from django.contrib.auth.models import AbstractBaseUser 
from django.db import models

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Album(models.Model):
    user = models.CharField(max_length=250, default="")
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class Material(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    thumbnail = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.title


class Cruzamentos(models.Model):
    gene_01 = models.CharField(max_length=40)
    gene_02 = models.CharField(max_length=40)
    gene_03 = models.CharField(max_length=40)
    gene_04 = models.CharField(max_length=40)

    def __unicode__(self):
        return self.gene_01 + ' - ' + self.gene_02 + ' - ' + self.gene_03 + ' - ' + self.gene_04

    

#class User(AbstractBaseUser):
    
    #username   = models.CharField(max_length=250)
    #avatar = models.ImageField()
    #email = models.CharField(max_length=250)
    #password = models.CharField(max_length=250)


    #USERNAME_FIELD = 'username'

    #def __str__(self):
       # return self.username + ' - ' + self.email
