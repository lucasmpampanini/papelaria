from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, default=None)
    email = models.EmailField(default=None, max_length=254)
    telefone = models.CharField(max_length=15, default=None)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=100, default=None)
    email = models.EmailField(default=None, max_length=254)
    telefone = models.CharField(max_length=15, default=None)

    def __str__(self):
        return self.nome
