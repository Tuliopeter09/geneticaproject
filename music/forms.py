from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Material, Cruzamentos

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ['title', 'pub_date', 'thumbnail']

class CruzamentosForm(forms.ModelForm):

    class Meta:
        model = Cruzamentos
        fields = ['gene_01', 'gene_02', 'gene_03', 'gene_04']








