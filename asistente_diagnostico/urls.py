from django.urls import path
from .views import *

app_name = 'asistente_diagnostico'

urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('afectacion-general', AfectacionGeneralView.as_view(), name='afectacion_general')
]
