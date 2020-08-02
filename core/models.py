from django.db import models

# Metodo 3
from django.contrib.auth import get_user_model
class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo

"""
Metodo 1
from django.contrib.auth.models import User
class Post(models.model):
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE())
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
"""

"""
# Metodo 2
from django.conf import settings
class Post(models.model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE())
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
"""

