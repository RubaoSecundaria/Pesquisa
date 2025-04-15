from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'atendimento_recepcao', 'atendimento_manicures', 'data_criacao')
    list_filter = ('dificuldade_totem', 'oferta_ajuda', 'limpeza_organizacao', 
                  'ambiente_climatizado', 'atendimento_recepcao', 'atendimento_manicures')
    search_fields = ('nome', 'sugestao_melhoria')
    readonly_fields = ('data_criacao',)
    date_hierarchy = 'data_criacao'
