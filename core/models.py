from django.db import models

# Create your models here.



class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100, null=False)
    email = models.EmailField('Email', null=False, max_length=100, unique=True)
    senha = models.CharField('Senha', max_length=64, null=False)


    def __str__(self):
        return self.nome
