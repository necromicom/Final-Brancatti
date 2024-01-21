from django.db import models


class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=10000)