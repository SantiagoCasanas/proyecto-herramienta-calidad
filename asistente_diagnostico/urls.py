from django.urls import path
from . import views
from .views import *


app_name = 'asistente_diagnostico'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('afectacion-general', ConsultarAfectacionGeneralView.as_view(), name='afectacion-general'),
    path('afectacion-general-detalle', AfectacionGeneralDetalleView.as_view(), name='afectacion-general-detalle')
]
