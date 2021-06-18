from django.shortcuts import render
from .forms import diarista_form


# Create your views here.

def cadastrar_diarista(request):
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST)
        if form_diarista.is_valid():
            form_diarista.save()
    form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})
