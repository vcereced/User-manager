from django.db import models

class Default(models.Model):
    name = models.CharField(max_length=100)  # Campo de texto
    fire = models.IntegerField()               # Campo entero para fuego
    water = models.IntegerField()              # Campo entero para agua
    ground = models.IntegerField()             # Campo entero para tierra
    description = models.TextField(blank=True) # Campo de texto, opcional
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Campo para subir imágenes

    def __str__(self):
        return self.name
