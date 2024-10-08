from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import FormView
from django.contrib import messages

#from django.views.generic import TemplateView

from asistente_diagnostico.models import AfectacionGeneral
from .models import AfectacionDetalladaInfraestructura
from .models import SueloSalinizacion
from .forms import AfectacionGeneralForm
from .models import Sodificacion
from .models import Salinizacion
from .models import AfectacionDetalladaIncrustracion
from .models import SalinizacionFao
from .models import PeligroMagnesio
from .models import Toxicidad

#from django.views.generic.detail import DetailView
from .funciones import obtener_recomendaciones_generales_infraestructura
from .funciones import encontrar_solucion
from .funciones import sales
from .funciones import salinizacion_lavado
from .funciones import condicion_sodicidad
from .funciones import anuncios
from .funciones import indice_langelier
from .funciones import peligro_magnesio
from .funciones import indice_ryznar
#from django.shortcuts import render, get_object_or_404
#from django.views import View



def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')



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

            #segunda tabla
            context['afectacion_infraestructura_dos'] = self.afectacion_infraestructura_dos
            context['valor_x']=self.valor_x

        if hasattr(self, 'sales_results'):
            context['sales_results'] = self.sales_results
            context['suelo_afectacion'] = self.suelo_afectacion
            context['yeso']=self.yeso
            context['top_3_sales'] = self.top_3_sales

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            
            parametros = form.cleaned_data
            context = self.get_context_data()
            
            limite, mensaje, limite_carbonatos_numero,mensaje_carbonatos, limite_ce_baja, mensaje_ce_baja, limite_ce_alta, mensaje_ce_alta = anuncios(parametros)
            
            # Generar el mensaje basado en el límite
            if limite == 1:
                messages.warning(request, mensaje)
            else:
                messages.success(request, mensaje)

            if limite_carbonatos_numero == 1:
                messages.warning(request, mensaje_carbonatos)
            else:
                messages.success(request, mensaje_carbonatos)

            if limite_ce_baja == 1:
                messages.warning(request, mensaje_ce_baja)
            else:
                messages.success(request, mensaje_ce_baja)
            
            if limite_ce_alta == 1:
                messages.warning(request, mensaje_ce_alta)
            else:
                messages.success(request, mensaje_ce_alta)


            self.anuncios = anuncios(form.cleaned_data)
            context['anuncios'] = self.anuncios 

            #########INFRAESTRUCTURA

            ###para la primera tabla
            self.valor_indice = obtener_recomendaciones_generales_infraestructura(parametros)
            self.afectacion_infraestructura = AfectacionGeneral.obtener_afectacion(self.valor_indice)
            context['afectacion_infraestructura'] = self.afectacion_infraestructura
            context['valor_indice'] = self.valor_indice
            
            ###para la segunda tabla 

            self.afectaciones_infraestructura_dos = []

            for parametros, valor in parametros.items():
                if valor is not None:  # Verifica que el valor no sea None
                    afectacion = AfectacionDetalladaInfraestructura.obtener_afectacion_infraestructura(parametros, valor)
                    if afectacion:
                        self.afectaciones_infraestructura_dos.append({
                            'parametro': parametros,
                            'valor_ingresado': valor,
                            'afectacion': afectacion
                        })
            context['afectaciones_infraestructura_dos'] = self.afectaciones_infraestructura_dos

            #incrustracion o corrosion 
            """ self.indice_langelier=indice_langelier(form.cleaned_data)
            context['indice_langelier']=self.indice_langelier
            print(indice_langelier)  
            """
        
            # Llama a la función para obtener datos adicionales
            resultado_funcion_adicional = indice_langelier(form.cleaned_data)

            ryznar_funcion_adicional = indice_ryznar(form.cleaned_data)
            print(f"Índice Ryznar: {ryznar_funcion_adicional}")
            
            # Asegúrate de que el resultado sea un diccionario
            if not isinstance(resultado_funcion_adicional, dict):
                raise ValueError("La función indice_langelier debe retornar un diccionario")
            
            if not isinstance(ryznar_funcion_adicional, dict):
                raise ValueError("La función indice_ryznar debe retornar un diccionario")
            
            # Combina el resultado de la función con el cleaned_data del formulario
            datos_combinados = {**form.cleaned_data, **resultado_funcion_adicional, **ryznar_funcion_adicional}
            print(f"Datos combinados: {datos_combinados}")

            # Procesa los datos combinados
            self.afectaciones_incrustracion = []

            for parametros, valor in datos_combinados.items():
            #for parametros, valor in {**form.cleaned_data, **resultado_funcion_adicional}.items():
                #print(f"Procesando {parametros}: {valor}")
                if valor is not None:  # Verifica que el valor no sea None

                    #afectacion_incrustracion = AfectacionDetalladaIncrustracion.obtener_afectacion_incrustracion(parametros, valor)

                    try:
                        afectacion_incrustracion = AfectacionDetalladaIncrustracion.obtener_afectacion_incrustracion(parametros, valor)
                    except Exception as e:
                        print(f"Error al procesar {parametros} con valor {valor}: {e}")
                        continue

                    if afectacion_incrustracion:
                        self.afectaciones_incrustracion.append({
                            'parametro': parametros,
                            'valor_ingresado': valor,
                            'afectacion_incrustracion': afectacion_incrustracion
                        })

            context['afectaciones_incrustracion'] = self.afectaciones_incrustracion
            
            

            #########SUELO 

            #para la recomendacion salinizacion 
            #FAO
            conductividad_electrica = form.cleaned_data['conductividad_electrica']
            salinizacion_fao = SalinizacionFao.SalinizacionFaoTabla(conductividad_electrica)
            #print(salinizacion_fao)
            context['salinizacion_fao'] = salinizacion_fao

            #SosalRiego

            riego_lavado = salinizacion_lavado(form.cleaned_data)
            self.riego_lavado_intento = salinizacion_lavado(form.cleaned_data)
            context['riego_lavado_intento'] = self.riego_lavado_intento
            

            self.riego_lavado_modelo = Salinizacion.salinizacion(riego_lavado)
            context['riego_lavado_modelo'] = self.riego_lavado_modelo
            sal=self.riego_lavado_modelo
            


            #ECHEVERRI
            self.sales_results = sales(form.cleaned_data)
            solubilidad = self.sales_results[4]
            top_3_sales = self.sales_results[5]
            context['top_3_sales'] = top_3_sales
            
            conductividad_electrica = form.cleaned_data.get('conductividad_electrica')
            self.conductividad_electrica = form.cleaned_data.get('conductividad_electrica')
            context['conductividad_electrica'] = self.conductividad_electrica
            #print (conductividad_electrica)

            self.suelo_afectacion = SueloSalinizacion.suelo_salinizacion(solubilidad, conductividad_electrica)

            context['sales_results'] = self.sales_results
            context['suelo_afectacion'] = self.suelo_afectacion

            suelo_afectacion = self.suelo_afectacion

            #Magnesium_hazard

            peligro_magnesio_valor = peligro_magnesio(form.cleaned_data)
            context['peligro_magnesio_valor']=peligro_magnesio_valor
            #print (f"peligro magnesio en views: {peligro_magnesio_valor}")
            
            suelo_magnesio = PeligroMagnesio.peligro_magnesio(peligro_magnesio_valor)
            #print (f"suelo_magnesio en views: {suelo_magnesio}")

            context['suelo_magnesio'] = suelo_magnesio


            

            """ self.solubilidad_sales = sales(parametros)
            self.solubilidad_sales_modelo= SueloSalinizacion.suelo_salinizacion(self.solubilidad_sales)
            context['solubilidad_sales_modelo'] = self.solubilidad_sales_modelo
             """
            
            

            #####para la recomendacion sodificacion
            
            resultado_condicion = condicion_sodicidad(form.cleaned_data)
        
            if isinstance(resultado_condicion, str):
                context['mensaje'] = resultado_condicion
                #print (resultado_condicion)
            else:
                self.valor_x = resultado_condicion
                context['valor_x'] = self.valor_x

                self.yeso = self.valor_x * 86
                context['yeso'] = self.yeso

                yeso = self.yeso

                self.yeso_modelo = Sodificacion.sodificacion(yeso)
                context['yeso_modelo'] = self.yeso_modelo
                #context['mensaje'] = "Recomendación: Aplicar enmiendas."


            """ Toxicidad """

            self.toxicidad_panel = []

            for parametros, valor in form.cleaned_data.items():
                if valor is not None:  # Verifica que el valor no sea None
                    toxicidad_panel = Toxicidad.toxicidad_planta(parametros, valor)
                    if toxicidad_panel:
                        self.toxicidad_panel.append({
                            'parametro': parametros,
                            'valor_ingresado': valor,
                            'afectacion': toxicidad_panel
                        })
            context['toxicidad_panel_1'] = self.toxicidad_panel
            print(f"Toxicidad: {self.toxicidad_panel}")

            # self.toxicidad_panel = Toxicidad.toxicidad_planta(form.cleaned_data)
            # toxicidad_panel = Toxicidad.toxicidad_planta(form.cleaned_data)
            
            # print(f"peligro magnesio en views: {self.toxicidad_panel}")
            # context['toxicidad_panel'] = self.toxicidad_panel





            #self.valor_x = encontrar_solucion(form.cleaned_data)  # Llamar a la nueva función
            """ self.valor_x = condicion_sodicidad(form.cleaned_data)
            context['valor_x'] = self.valor_x 
            valor_x = self.valor_x 
            print(valor_x)

            self.yeso=self.valor_x*86
            context['yeso']=self.yeso
            yeso=self.yeso

            self.yeso_modelo= Sodificacion.sodificacion(yeso)
            context['yeso_modelo']=self.yeso_modelo """

            #

            #riego = salinizacion(form.cleaned_data)
            #print(riego)
            
            
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








""""

#######################
class AfectacionGeneralDetalleView(TemplateView):
    template_name = "afectacion_general_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valor_indice'] = self.request.session.get('valor_indice')
        context['afectaciones'] = self.request.session.get('afectaciones')
        return context



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

"""