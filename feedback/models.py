from django.db import models

class Feedback(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    dificuldade_totem = models.CharField(max_length=20)
    oferta_ajuda = models.CharField(max_length=20)
    limpeza_organizacao = models.CharField(max_length=20)
    ambiente_climatizado = models.CharField(max_length=20)
    atendimento_recepcao = models.CharField(max_length=20)
    atendimento_manicures = models.CharField(max_length=20)
    sugestao_melhoria = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback de {self.nome} - {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"