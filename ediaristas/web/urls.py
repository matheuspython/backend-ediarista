from django.urls import path
from .views import cadastrar_diarista

urlpatterns = [
    path('cadastrar_diarista', cadastrar_diarista, name='cadastrar_diarista'),
    path('listar_diaristas', cadastrar_diarista, name='cadastrar_diarista'),
]
