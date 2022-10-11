from contextlib import redirect_stderr
from email import message
from typing import List
from django.shortcuts import render, redirect
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

def simulation_items(request):
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
        return render(request, 'simulation_items.html',{})

def delete_simulation(request, simulation_id):
    simulacao = Simulacao.objects.get(pk=simulation_id)
    simulacao.delete()
    return redirect('simulations')


def edit_simulation(request, simulation_id):
    if request.method == 'POST':
        form = NovaSimulacao(request.POST )
        if form.is_valid():
            form.save()
        #form = NovaSimulacao()
    else:
        simulacao = Simulacao.objects.get(pk=simulation_id)
        form = NovaSimulacao(instance=simulacao)
    todas_simulacoes = Simulacao.objects.all
    return render(request, 'simulations.html',{'form': form,'todas_simulacoes':todas_simulacoes})



def delete_items(request):
    return render(request, 'simulation_items.html',{})

def edit_items(request):
    return render(request, 'simulation_items.html',{})