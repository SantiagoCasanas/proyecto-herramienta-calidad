from django.urls import path
from . import views
from .views import *
#from .views import AfectacionGeneralDetailView
#from .views import AfectacionGeneralView



app_name = 'asistente_diagnostico'

urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('afectacion-general', AfectacionGeneralView.as_view(), name='afectacion-general'),
    path('afectacion-general-detalle', AfectacionGeneralDetalleView.as_view(), name='afectacion-general-detalle'),
    #path('afectacion_general_detalle/<int:pk>/', AfectacionGeneralDetailView.as_view(), name='afectacion_general_detalle'),
    #path('prueba', ResultadosView.as_view(), name='prueba'),
    #path('afectacion/comparar/<int:pk>/', AfectacionGeneralView.as_view(), name='comparar_valores'),
]
