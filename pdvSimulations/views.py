from typing import List
from django.shortcuts import render
from .models import Simulacao,Itens_Simulacao
from .forms import NovaSimulacao,NovoItem
from django.http import HttpResponseRedirect

def simulations(request):
    if request.method == 'POST':
        form = NovaSimulacao(request.POST or None)
        if form.is_valid():
            form.save()

    form = NovaSimulacao()
    todas_simulacoes = Simulacao.objects.all
    return render(request, 'simulations.html',{'form': form,'todas_simulacoes':todas_simulacoes})

def newsimulation(request):
    submitted = False
    if request.method == 'POST':
        form = NovaSimulacao(request.POST or None)
        if form.is_valid():
            form.save()
        
        todas_simulacoes = Simulacao.objects.all
        return render(request, 'simulations.html',{'todas_simulacoes':todas_simulacoes})        
    else:
        form = NovaSimulacao()
        todas_itens = Itens_Simulacao.objects.all
        context = {'form': form,'submitted':submitted}
        return render(request, 'newsimulation.html',{})

def newitem(request):
    return render(request, 'newitem.html',{})
