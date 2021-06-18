from django.shortcuts import render
from .forms import diarista_form
from .models import Diarista

# Create your views here.

def cadastrar_diarista(request):
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
    else:
        form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})


def listar_diaristas(request):
    diaristas = Diarista.objects.all()
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})