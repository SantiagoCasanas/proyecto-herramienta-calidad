from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import AfectacionGeneral
from .forms import AfectacionGeneralForm


def inicio(request):
    return render(request, 'inicio.html')


class AfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('asistente_diagnostico:afectacion_general')

    def form_valid(self, form):
        #accedo a valores registrados por el usuario
        valor_referencia = form.cleaned_data['valor']
        print(valor_referencia)
        
        print(f'El valor de referencia es: {AfectacionGeneral.obtener_afectacion(valor_referencia)}')
        funcion_maria(valor_referencia)
        return super().form_valid(form)
    


def funcion_maria(valores):
    pass