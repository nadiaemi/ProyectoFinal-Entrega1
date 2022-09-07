from django.db import models

# Create your models here.

class Comidas (models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre +' - '+ self.marca +' - $ '+ str(self.precio)


class Bebidas (models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre +' - '+ self.marca +' - $ '+ str(self.precio)

   
class Otros (models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre +' - '+ self.marca +' - $ '+ str(self.precio)