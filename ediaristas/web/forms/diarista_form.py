from django import forms
from ..models import Diarista

class DiaristaForm(forms.ModelForm):
    model = Diarista
    fiels = '__all__'
