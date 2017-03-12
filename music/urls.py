from django.conf.urls import url
from . import views
from django.contrib import admin
#from django.contrib.auth.views import password_reset, password_reset_done
#from django.contrib.auth.views import *
#from django.contrib.auth.views import password_reset, password_reset_done
#from django.views.generic import direct_to_template
admin.autodiscover()

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^etapa_01/$', views.etapa_01, name='etapa_01'),
    url(r'^etapa_02/$', views.etapa_02, name='etapa_02'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    url(r'^resetpassword/passwordsent/$', views.password_reset_done), 
    url(r'^resetpassword/$', views.password_reset), 
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm),
    url(r'^reset/done/$', views.password_reset_complete),
    #url(r'^direct/$', direct_to_template, {'template': 'direct.html', 'extra_context': {'showDirect': True}}),  
    url(r'^primeiralei/$', views.primeiralei, name='primeiralei'),
    url(r'^primeiralei_resultado/$', views.primeiralei_resultado, name='primeiralei_resultado'),
    url(r'^mendelprimeiralei/$', views.mendelprimeiralei, name='mendelprimeiralei'),
    



]

