from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Feedback

def feedback_form(request):
    return render(request, 'forms.html')

def enviar_feedback(request):
    if request.method == 'POST':
        # Coletar dados do formulário
        nome = request.POST.get('nome')
        dificuldade_totem = request.POST.get('dificuldade_totem')
        oferta_ajuda = request.POST.get('oferta_ajuda')
        limpeza_organizacao = request.POST.get('limpeza_organizacao')
        ambiente_climatizado = request.POST.get('ambiente_climatizado')
        atendimento_recepcao = request.POST.get('atendimento_recepcao')
        atendimento_manicures = request.POST.get('atendimento_manicures')
        sugestao_melhoria = request.POST.get('sugestao_melhoria')
        
        # Criar novo objeto Feedback
        Feedback.objects.create(
            nome=nome,
            dificuldade_totem=dificuldade_totem,
            oferta_ajuda=oferta_ajuda,
            limpeza_organizacao=limpeza_organizacao,
            ambiente_climatizado=ambiente_climatizado,
            atendimento_recepcao=atendimento_recepcao,
            atendimento_manicures=atendimento_manicures,
            sugestao_melhoria=sugestao_melhoria
        )
        
        # Redirecionar para página de agradecimento
        return redirect('thank_you')
    
    # Se não for POST, redirecionar para o formulário
    return redirect('feedback_form')

def thank_you(request):
    return render(request, 'thank_you.html')

class RespostasPesquisaView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Feedback
    template_name = 'respostas.html'
    context_object_name = 'feedbacks'
    ordering = ['-data_criacao']
    paginate_by = 10
    
    # Redireciona para login se não estiver autenticado
    login_url = '/admin/login/'
    
    # Verifica se o usuário é superusuário (admin)
    def test_func(self):
        return self.request.user.is_superuser