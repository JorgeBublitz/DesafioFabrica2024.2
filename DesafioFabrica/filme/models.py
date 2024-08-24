from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.CharField(max_length=10)
    diretor = models.CharField(max_length=255)
    sinopse = models.TextField()
    url_poster = models.URLField()
    avaliacao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
