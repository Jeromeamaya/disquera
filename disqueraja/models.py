from django.db import models

# Create your models here.
class Disquera(models.Model):
    id=models.AutoField(primary_key=True)
    nitdisquera=models.CharField( max_length=50)
    nombredisquera=models.CharField( max_length=100)
    telefonodisquera=models.CharField( max_length=15) 
    direcciondisquera=models.CharField( max_length=100)
    estadodisquera=models.BooleanField()
    
class Artista(models.Model):
    id=models.AutoField(primary_key=True)
    iddisqierafk=models.ForeignKey(Disquera,on_delete=models.CASCADE)
    nomdocumento=models.CharField(max_length=20)
    tipodocumento=models.CharField(max_length=20)
    nombreartista=models.CharField(max_length=50)
    apellidoartista=models.CharField(max_length=50)
    nombreartistico=models.CharField(max_length=50)
    fnacimartista=models.DateField()
    emailartista=models.CharField(max_length=100)
    fotoartista=models.CharField(max_length=255)
    estadoartista=models.BooleanField()

class Genero(models.Model):
    id=models.AutoField(primary_key=True)    
    nombregenero=models.CharField(max_length=100)
    estadogenero=models.BooleanField()
class Album(models.Model):
    id=models.AutoField(primary_key=True)    
    idartistafk=models.ForeignKey(Artista,on_delete=models.CASCADE)
    idgenerofk=models.ForeignKey(Genero,on_delete=models.CASCADE)
    nombrealbum=models.CharField(max_length=100)
    aniopublicacion=models.CharField(max_length=5)
    fotoalbum=models.CharField(max_length=255)
    estadoalbum=models.BooleanField()
    
class Cancion(models.Model):
    id=models.AutoField(primary_key=True)
    idalbumfk=models.ForeignKey(Album,on_delete=models.CASCADE) 
    nombrecancion=models.CharField(max_length=100)
    duracioncancion=models.IntegerField()
    estadocancion=models.BooleanField()
    
     

        