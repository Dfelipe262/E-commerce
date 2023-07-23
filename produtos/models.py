from django.db import models

class Produto(models.Model):

    ROLE_CHOICES = (
        ('Notebook', 'Notebook'),
        ('Celular', 'Celular'),
        ('Acessorio', 'Acessório'),
        ('Camera', 'Câmera'),
    )

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True )
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='static/img', null = True, blank=True)


# Create your models here.
