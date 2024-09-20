from django.db import models 

class Produto(models.Model)
        codigoProduto = models.CharField(max_lenght=255)
        tituloProduto = models.CharField(max_lenght=255)
        preco = models.DecimalField(max-digits=10, decimal_places=2)
        descricao = models.Charfield(max_lenght=255)
        imagemProduto = models.Charfield(max_lenght=255)
        categoriaProduto = models.Charfield(max_lenght=255)
        classificacaoProduto= models.DecimalField(max_digits=10)
        exibirHome = models.BooleanField(default=True)