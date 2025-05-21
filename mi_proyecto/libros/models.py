from django.db import models
from django.contrib.auth.models import User

# TABLA AUTOR
class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username 


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publicado = models.DateField()
    
    def __str__(self):
        return self.titulo