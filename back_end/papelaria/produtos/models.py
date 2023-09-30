from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    percentual_comissao = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao
