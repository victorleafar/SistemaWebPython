from django.db import models
from django.contrib.auth.models import Group

class Produto(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return self.descricao