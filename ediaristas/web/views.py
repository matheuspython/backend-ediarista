from django.shortcuts import render
from .forms import diarista_form

# Create your views here.

def cadastrar_diarista(req):
    form_diarista = diarista_form()
    return render(req, 'form_diarista.html', {'form_diarista': form_diarista})