from django.urls import path
from asistente_diagnostico import views
from .views import *


app_name = 'asistente_diagnostico'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('afectacion-general', ConsultarAfectacionGeneralView.as_view(), name='afectacion-general'),
    #path('afectacion-general-detalle', AfectacionGeneralDetalleView.as_view(), name='afectacion-general-detalle')
]
