from django.db import models
from pessoas.models import Cliente, Vendedor
from produtos.models import Produto
    
class Venda(models.Model):
    numero_nota_fiscal = models.CharField(max_length=20)
    data_hora = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemVenda')

    def __str__(self):
        return self.numero_nota_fiscal

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

class ConfiguracaoComissao(models.Model):
    dia_semana = models.IntegerField(choices=[
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ])
    percentual_minimo = models.DecimalField(max_digits=4, decimal_places=2)
    percentual_maximo = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.dia_semana