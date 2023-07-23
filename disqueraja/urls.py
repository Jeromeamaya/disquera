from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('artista',views.artista,name='artista'),
    path('artista/add',views.addartista,name='artista-add'),
    path('artista/edit',views.editartista,name='artista-edit'),
    path('cancion',views.cancion,name='cancion'),
    path('cancion/add',views.addcancion,name='cancion-add'),
    path('cancion/edit',views.editcancion,name='cancion-edit'),
    path('album',views.album,name='album'),
    path('album/add',views.addalbum,name='album-add'),
    path('album/edit',views.editalbum,name='album-edit'),
    path('disquera',views.disquera,name='disquera'),
    path('disquera/add',views.adddisquera,name='disquera-add'),
    path('disquera/edit',views.editdisquera,name='disquera-edit'),
    path('genero',views.genero,name='genero'),
    path('genero/add',views.addgenero,name='genero-add'),
    path('genero/edit',views.editgenero,name='genero-edit')

    
]
