from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
#from django.views.generic.detail import DetailView
from .funciones import obtener_recomendaciones_generales_infraestructura
#from django.shortcuts import render, get_object_or_404
#from django.views import View


from .models import AfectacionGeneral
from .forms import AfectacionGeneralForm


def inicio(request):
    return render(request, 'inicio.html')


class ConsultarAfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('afectacion-general')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #guarda los datos de contexto para el html
        if hasattr(self, 'afectacion_infraestructura'):
            context['afectacion_infraestructura'] = self.afectacion_infraestructura
            #context['afectacion_segunda_tabla'] = self.afectacion_segunda_tabla
            context['valor_indice'] = self.valor_indice
            #context['indice_helier'] = self.indice_helier
        
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            parametros = form.cleaned_data
            context = self.get_context_data()

            ###para la primera tabla
            self.valor_indice = obtener_recomendaciones_generales_infraestructura(parametros)
            self.afectacion_infraestructura = AfectacionGeneral.obtener_afectacion(self.valor_indice)
            context['afectacion_infraestructura'] = self.afectacion_infraestructura
            context['valor_indice'] = self.valor_indice
            
            #### para langelier
            #self.valor_indice_helier = obtener_indice_helier(parametros)
            #self.indice_helier = Modelo.objects.filter(parametro="Índice de Langelier", valor_minimo__lte=self.valor_indice_helier, valor_maximo__gte=self.valor_indice_helier).first()
            #context['indice_helier'] = self.indice_helier
            
            ###para demas parametros
            #self.ph_valor = parametros["ph"]
            #self.ph = Modelo.objects.filter(parametro="PH", valor_minimo__lte=self.ph_valor, valor_maximo__gte=self.ph_valor).first()
            ##para cada parametro

           
            return self.render_to_response(context)
        else:
            return self.form_invalid(form)





    
class AfectacionGeneralDetalleView(TemplateView):
    template_name = "afectacion_general_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valor_indice'] = self.request.session.get('valor_indice')
        context['afectaciones'] = self.request.session.get('afectaciones')
        return context


""""

Lo entrega abajo del formulario
class AfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('asistente_diagnostico:afectacion-general')

    def form_valid(self, form):
        # Extraer los parámetros del formulario
        parametros = form.cleaned_data

        # Obtener el valor del índice basado en los valores del formulario
        valor_indice = obtener_recomendaciones_generales_infraestructura(parametros)

        # Obtener datos del modelo AfectacionGeneral correspondientes al valor del índice
        # Filtramos los registros basándonos en el valor del índice. 
        afectaciones = AfectacionGeneral.objects.filter(valor_minimo__lte=valor_indice, valor_maximo__gte=valor_indice)

        # Pasar datos al contexto
        context = self.get_context_data()
        context['valor_indice'] = valor_indice
        context['afectaciones'] = afectaciones
        return self.render_to_response(context)
       




class AfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('asistente_diagnostico:afectacion-general')

    def form_valid(self, form):
        # Extraer los parámetros del formulario
        parametros = form.cleaned_data

        # Obtener valor del indice basadas en los valores del formulario
        valor_indice = obtener_recomendaciones_generales_infraestructura(parametros)

        print(f'Recomendaciones: {valor_indice}')
        
        
                # Obtener todas las recomendaciones del modelo
        recomendaciones_modelo = AfectacionGeneral.objects.all()

        # Crear una lista de diccionarios para pasar a la plantilla
        recomendaciones_context = []
        for recomendacion in recomendaciones_modelo:
            recomendaciones_context.append({

                'valor_minimo': recomendacion.valor_minimo,
                'valor_maximo': recomendacion.valor_maximo,
                'nivel_afectacion': recomendacion.nivel_afectacion,
                'recomendacion': recomendacion.recomendacion
            })

        context = self.get_context_data(form=form)
        context['recomendaciones'] = recomendaciones_context

        return self.render_to_response(context)



class AfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('asistente_diagnostico:afectacion-general')

    def form_valid(self, form):
        # Imprimir todos los valores del formulario
        for field_name, value in form.cleaned_data.items():
            print(f'{field_name}: {value}')
        
        # Extraer los parámetros del formulario
        parametros = form.cleaned_data

        # Obtener recomendaciones basadas en los valores del formulario
        recomendaciones = obtener_recomendaciones_generales_infraestructura(parametros)
        print(f'Recomendaciones: {recomendaciones}')

        # Continuar con el flujo normal de form_valid
        return super().form_valid(form)





class AfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('asistente_diagnostico:afectacion-general')

    def form_valid(self, form):
        # Guardar los valores del formulario en el contexto
        context = self.get_context_data(form=form)
        context['form_data'] = form.cleaned_data

        parametros= form.cleaned_data


        #valor_referencia = form.cleaned_data['ph']
        #print(f'El valor de referencia es: {AfectacionGeneral.obtener_afectacion(valor_referencia)}')

        recomendaciones = obtener_recomendaciones_generales_infraestructura(parametros)
        context['recomendaciones'] = recomendaciones

        
        # Renderizar el template con los valores del formulario
        return self.render_to_response(context)





class AfectacionGeneralView(FormView):
    template_name = "afectacion.html"
    form_class = AfectacionGeneralForm
    success_url = reverse_lazy('asistente_diagnostico:afectacion-general')

    def form_valid(self, form):
        #accedo a valores registrados por el usuario
        valor_referencia = form.cleaned_data['ph']
        print(valor_referencia)
        
        print(f'El valor de referencia es: {AfectacionGeneral.obtener_afectacion(valor_referencia)}')
        funcion_maria(valor_referencia)
        return super().form_valid(form)



#lo agregué
class ResultadosView(TemplateView):
    template_name = 'prueba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valor_referencia'] = self.request.session.get('valor_referencia', 'No disponible')
        context['afectacion'] = self.request.session.get('afectacion', 'No disponible')
        
        # Limpiar los datos de la sesión después de mostrar
        self.request.session.pop('valor_referencia', None)
        self.request.session.pop('afectacion', None)
        
        return context



def funcion_maria(valores):
    pass


class AfectacionGeneralDetailView(DetailView):
    model = AfectacionGeneral
    template_name = 'afectacion_general_detalle.html'
    context_object_name = 'afectacion_general_detalle'
"""