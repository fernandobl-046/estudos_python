import uuid
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract=True

class Contato(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    conteudo = models.TextField()

    def __str__(self):
        return self.nome

class Carro(BaseModel):
    marca = models.TextField("Marca do carro", max_length=100)
    ano = models.PositiveIntegerField("Ano")
    cor = models.CharField(max_length=10)
    combustivel = models.CharField(max_length=10)

    def __str__(self):
        return self.marca
