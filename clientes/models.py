from django.db import models
from uuid import uuid4


class Emprestimos(models.Model):

    id_client = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    cpf = models.IntegerField()
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=400)
    valor = models.FloatField()
    status = models.CharField(max_length=50, default='pendente')
    data_solicitado = models.DateTimeField(auto_now_add=True)
