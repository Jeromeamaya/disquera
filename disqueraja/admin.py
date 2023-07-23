from django.contrib import admin
from .models import Artista
from .models import Disquera
from .models import Album
from .models import Genero
from .models import Cancion

admin.site.register(Disquera)
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(Cancion)




# Register your models here.


