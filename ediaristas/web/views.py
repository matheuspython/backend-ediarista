from django.shortcuts import render
from .forms import diarista_form


# Create your views here.

def cadastrar_diarista(request):
    form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})
