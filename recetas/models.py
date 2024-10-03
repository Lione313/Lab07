from django.db import models
from django.contrib.auth.models import User
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email + ','+ self.nombre


class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f'Titulo: {self.titulo}, Ingredientes: {self.ingredientes}, Preparación: {self.preparacion}, Autor: {self.autor.nombre}'


class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    texto = models.TextField(help_text='Tú comentario', verbose_name='Comentario')

    def __str__(self):
        return f'Receta: {self.receta.titulo}, Comentario: {self.texto}'
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_organizados')

    def __str__(self):
        return self.nombre
class RegistroEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='registros')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='registros')

    def __str__(self):
        return f'{self.usuario.nombre} - {self.evento.nombre}'
