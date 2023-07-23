from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1> Bienvenido a la Disquera </h1>")
def pagina1(request):
    return render(request,'views/pagina1.html')
# vistas disquera de la carpeta album.


def album(request):
    return render(request,'album/index.html')
def addalbum(request):
    return render(request,'album/crear.html')
def editalbum(request):
    return render(request,'album/editar.html')



# vistas disquera de la carpeta artista.
def artista(request):
    return render(request,'artista/index.html')
def addartista(request):
    return render(request,'artista/crear.html')
def editartista(request):
    return render(request,'artista/editar.html')


# vistas disquera de la carpeta cancion.


def cancion(request):
    return render(request,'cancion/index.html')
def addcancion(request):
    return render(request,'cancion/crear.html')
def editcancion(request):
    return render(request,'cancion/editar.html')



# vistas disquera de la carpeta disquera.

def disquera(request):
    return render(request,'disquera/index.html')
def adddisquera(request):
    return render(request,'disquera/crear.html')
def editdisquera(request):
    return render(request,'disquera/editar.html')



# vistas disquera de la carpeta genero.
def genero(request):
    return render(request,'genero/index.html')
def addgenero(request):
    return render(request,'genero/crear.html')
def editgenero(request):
    return render(request,'genero/editar.html')
