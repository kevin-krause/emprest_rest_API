from rest_framework import serializers
from clientes import models


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emprestimos
        fields = '__all__'
