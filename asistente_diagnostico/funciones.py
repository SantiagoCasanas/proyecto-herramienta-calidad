
import numpy as np
from scipy.optimize import fsolve
#from .models import *
from asistente_diagnostico.models import AfectacionDetalladaInfraestructura
from scipy.optimize import root
import math

#Activamos el ambiente: source venv/Scripts/activate
#Corremos el proyecto: python manage.py runserver

#En general 

def anuncios(parametros):

    ph = parametros["ph"]
    calcio = conversion(parametros["calcio"], 'calcio')
    magnesio = conversion(parametros["magnesio"], 'magnesio')
    sodio = conversion(parametros["sodio"], 'sodio')
    potasio = conversion(parametros["potasio"], 'potasio')
    conductividad = parametros["conductividad_electrica"]
    

    carbonato = conversion(parametros["carbonato"], 'carbonato')
    bicarbonato = conversion(parametros["bicarbonato"], 'bicarbonato')
    cloro= conversion(parametros["cloro"], 'cloro')
    sulfatos = conversion(parametros["sulfatos"], 'sulfatos')



    suma_cationes = (calcio+magnesio+sodio+potasio)
   
    suma_aniones = (carbonato+bicarbonato+cloro+sulfatos)
    
    diferencia = abs(suma_cationes - suma_aniones)
    diferencia_relativa = (diferencia*100)/ ((suma_cationes + suma_aniones))
    
    conductividad_limite = (suma_aniones + suma_cationes)/2
    print(conductividad_limite)



    limite=""
    mensaje = ""
    limite_carbonatos_numero=""
    mensaje_carbonato=""
    limite_ce_baja=""
    mensaje_ce_baja=""
    limite_ce_alta=""
    mensaje_ce_alta=""

    if ph>8.2 and carbonato<=0:
        limite_carbonatos_numero = 1
        mensaje_carbonato = "Los carbonatos deben de ser mayores a cero"
    

    if diferencia_relativa > 10:
        limite = 1
        mensaje = "La diferencia entre la suma de cationes y aniones es mayor al 10%. Revisar"

    if (0.06 * conductividad_limite) > conductividad:
        limite_ce_baja= 1
        mensaje_ce_baja = "CEr muy baja"
    
    if (0.12 * conductividad_limite) < conductividad:
        limite_ce_alta = 1
        mensaje_ce_alta = "CEr muy alta"
        
    return limite, mensaje,  limite_carbonatos_numero, mensaje_carbonato, limite_ce_baja, mensaje_ce_baja, limite_ce_alta, mensaje_ce_alta 



#INFRAESTRUCTURA

def obtener_recomendaciones_generales_infraestructura( parametros):

    fuente_abastecimiento = parametros["fuentes_abastecimiento"]
    conductividad = parametros["conductividad_electrica"]
    ph = parametros["ph"]
    solidos_disueltos = parametros["solidos_disueltos"]
    solidos_solubles = parametros["solidos_solubles"]
    hierro = parametros["hierro"]
    manganeso = parametros["manganeso"]
    magnesio = parametros["magnesio"]
    nitrogeno = parametros["nitrogeno"]
    amonio = parametros["amonio"]
    sulfatos = parametros["sulfatos"]
    temperatura = parametros["temperatura"]
    alcalinidad = parametros["alcalinidad"]
    dureza = parametros["dureza"]
    
    indice_langelier = temperatura+ph+alcalinidad+dureza-12.5

    if solidos_solubles<50:
        valor_normalizado_ss=0.33
    elif solidos_solubles>=50 and solidos_solubles<=100:
        valor_normalizado_ss=0.66
    else:
        valor_normalizado_ss=1

    if solidos_disueltos<500:
        valor_normalizado_sd=0.33
    elif solidos_solubles>=500 and solidos_solubles<=2000:
        valor_normalizado_sd=0.66
    else:
        valor_normalizado_sd=    1

    if hierro<0.2:    
        valor_normalizado_hierro=0.33
    elif hierro>=0.2 and hierro<=1.5:
        valor_normalizado_hierro=0.66
    else:
        valor_normalizado_hierro=1

    if manganeso<0.1:
        valor_normalizado_manganeso=0.33
    elif manganeso>=0.1 and manganeso<=1.5:
        valor_normalizado_manganeso=0.66
    else:
        valor_normalizado_manganeso=1

    if nitrogeno<0.5:
        valor_normalizado_nitrogeno=0.33
    elif hierro>=0.5 and solidos_solubles<=2.5:
        valor_normalizado_nitrogeno=0.66
    else:
        valor_normalizado_nitrogeno=1    

    if ph<6.5:
        valor_normalizado_ph=0.33
    elif ph>=6.5 and ph<=8.4:
        valor_normalizado_ph=0.66
    else:
        valor_normalizado_ph=1  

    if sulfatos<200:
        valor_normalizado_sulfatos=0.25
    elif sulfatos>=200 and sulfatos<600:
        valor_normalizado_sulfatos=0.5
    elif sulfatos>=600 and sulfatos<=3000:
        valor_normalizado_sulfatos=0.75
    else:
        valor_normalizado_sulfatos=1

    if magnesio<100:
        valor_normalizado_magnesio=0.25
    elif magnesio>=100 and magnesio<300:
        valor_normalizado_magnesio=0.5
    elif magnesio>=300 and magnesio<=1500:
        valor_normalizado_magnesio=0.75
    else:
        valor_normalizado_magnesio=1
    
    if indice_langelier<=-2:
        valor_normalizado_langelier=1
    elif indice_langelier>-2 and indice_langelier<=-0.4:
        valor_normalizado_langelier=0.66
    elif indice_langelier>-0.4 and indice_langelier<=0.4:
        valor_normalizado_langelier=0.33
    elif indice_langelier>0.4 and indice_langelier<=2:
        valor_normalizado_langelier=0.66
    else:
        valor_normalizado_langelier=1  

    if fuente_abastecimiento== "superficial":
        valor_indice= (0.19*valor_normalizado_ss)+(0.03*valor_normalizado_sd)+\
        (0.1*valor_normalizado_hierro)+(0.2*valor_normalizado_manganeso)+\
        (0.05*valor_normalizado_nitrogeno)+(0.02*valor_normalizado_ph)+\
        (0.22*valor_normalizado_sulfatos)+(0.15*valor_normalizado_magnesio)+\
        (0.04*valor_normalizado_langelier)

    elif fuente_abastecimiento=="subterranea":
        valor_indice= (0.28*valor_normalizado_ss)+(0.01*valor_normalizado_sd)+\
        (0.01*valor_normalizado_hierro)+(0.03*valor_normalizado_manganeso)+\
        (0.04*valor_normalizado_nitrogeno)+(0.04*valor_normalizado_ph)+\
        (0.24*valor_normalizado_sulfatos)+(0.27*valor_normalizado_magnesio)+\
        (0.08*valor_normalizado_langelier)

    try:
        return valor_indice
        #recomendaciones = AfectacionGeneral.obtener_afectacion(valor_indice)
        #return recomendaciones
    
    except:
        return None
    

def indice_langelier(parametros):

    ph = parametros["ph"]
    temperatura = parametros["temperatura"]
    alcalinidad = parametros["alcalinidad"]
    dureza = parametros["dureza"]
    calcio = parametros["calcio"]
    solidos_disueltos = parametros["solidos_disueltos"]


    A = (math.log10(solidos_disueltos)-1)/10
    print(f"A: {A}")
    B = (-13.12 * math.log10(temperatura +273)) + 34.55
    print(f"B: {B}")
    C = math.log10(2.5*calcio) - 0.4
    print(f"C: {C}")
    D = math.log10(alcalinidad)
    print(f"D: {D}")

    ph_s = (9.3 + A + B) - (C + D)
    
    indice_langelier = ph - ph_s
    
    print(f"indice de langelier: {indice_langelier}")
    
    return {"indice_langelier": indice_langelier}


def indice_ryznar(parametros):

    ph = parametros["ph"]
    temperatura = parametros["temperatura"]
    alcalinidad = parametros["alcalinidad"]
    dureza = parametros["dureza"]
    calcio = parametros["calcio"]
    solidos_disueltos = parametros["solidos_disueltos"]


    A = (math.log10(solidos_disueltos)-1)/10
    print(f"A: {A}")
    B = (-13.12 * math.log10(temperatura +273)) + 34.55
    print(f"B: {B}")
    C = math.log10(2.5*calcio) - 0.4
    print(f"C: {C}")
    D = math.log10(alcalinidad)
    print(f"D: {D}")

    ph_s = (9.3 + A + B) - (C + D)
    
    indice_ryznar = 2*ph_s - ph
    
    print(f"Índice Ryznar: {indice_ryznar}")
    return {'indice_ryznar': indice_ryznar}

#SUELO

#######indice o tabla 1

def indice_suelo (parametros):

    fuente_abastecimiento = parametros["fuentes_abastecimiento"]
    conductividad = parametros["conductividad_electrica"]
    carbonato_sodico_residual = parametros["carbonato_sodico_residual"]
    porcentaje_sodio_soluble = parametros["porcentaje_sodio_soluble"]
    
    if carbonato_sodico_residual<1.25:
        valor_normalizado_cabonato_sodico_residual=0.2
    elif carbonato_sodico_residual>=1.25 and carbonato_sodico_residual<2:
        valor_normalizado_cabonato_sodico_residual=0.4
    elif carbonato_sodico_residual>=2 and carbonato_sodico_residual<2.5:
        valor_normalizado_cabonato_sodico_residual=0.6
    elif carbonato_sodico_residual>=2.5 and carbonato_sodico_residual<=3:
        valor_normalizado_cabonato_sodico_residual=0.8
    else:
        valor_normalizado_cabonato_sodico_residual=1

    if porcentaje_sodio_soluble<20:
        valor_normalizado_porcentaje_sodio_soluble=0.2
    elif porcentaje_sodio_soluble>=20 and porcentaje_sodio_soluble<40:
        valor_normalizado_porcentaje_sodio_soluble=0.4
    elif porcentaje_sodio_soluble>=40 and porcentaje_sodio_soluble<60:
        valor_normalizado_porcentaje_sodio_soluble=0.6
    elif porcentaje_sodio_soluble>=60 and porcentaje_sodio_soluble<=80:
        valor_normalizado_porcentaje_sodio_soluble=0.8
    else:
        valor_normalizado_porcentaje_sodio_soluble=1

 

    if fuente_abastecimiento== "superficial":
        valor_indice_suelo= (0.35*valor_normalizado_porcentaje_sodio_soluble)+\
        (0.07*valor_normalizado_cabonato_sodico_residual)
        

    elif fuente_abastecimiento=="subterranea":
        valor_indice_suelo= (0.41*valor_normalizado_porcentaje_sodio_soluble)+\
        (0.09*valor_normalizado_cabonato_sodico_residual)
       
    try:
        return valor_indice_suelo
        #recomendaciones = AfectacionGeneral.obtener_afectacion(valor_indice)
        #return recomendaciones
    
    except:
        return None
    
def conversion(mg_per_l, soluto):
    solutos_data = {
        'sodio': 22.99 / 1, 
        'calcio': 40.08 / 2,
        'potasio': 39.10 / 1,
        'magnesio': 24.31 / 2,
        'sulfatos': 96.06 / 2,
        'cloro': 35.45 / 1,
        'carbonato': 60.01 / 2,
        'bicarbonato': 61.02 / 1
    }

    peso_equivalente = solutos_data[soluto]
    mmolc_per_l = mg_per_l / peso_equivalente
    #print(f"Conversión: {mg_per_l} mg/L de {soluto} a {mmolc_per_l} mmolc/L")
    return mmolc_per_l

def sales (parametros):

    ##################
    calcio = conversion(parametros["calcio"], "calcio")
    magnesio = conversion(parametros["magnesio"], "magnesio")
    sodio = conversion(parametros["sodio"], "sodio")
    potasio = conversion(parametros["potasio"], "potasio")
    carbonato = conversion(parametros["carbonato"], "carbonato")
    bicarbonato = conversion(parametros["bicarbonato"], "bicarbonato")
    cloro = conversion(parametros["cloro"], "cloro")
    sulfatos = conversion(parametros["sulfatos"], "sulfatos")
    #mmol
   

    if calcio>carbonato: 
        carbonato_calcio=carbonato
    else:
        carbonato_calcio=calcio
    

    if magnesio>(carbonato-carbonato_calcio): 
        carbonato_magnesio=carbonato-carbonato_calcio
    else:
        carbonato_magnesio=magnesio
    
    if bicarbonato>calcio-(carbonato_calcio): 
        bicarbonato_calcio=calcio-(carbonato_calcio)
    else:
        bicarbonato_calcio=bicarbonato

    if (bicarbonato-bicarbonato_calcio)>(magnesio-carbonato_magnesio): 
        bicarbonato_magnesio=magnesio-carbonato_magnesio
    else:
        bicarbonato_magnesio=bicarbonato-bicarbonato_calcio

    if (calcio-carbonato_calcio-bicarbonato_calcio)>sulfatos: 
        sulfato_calcio=sulfatos
    else:
        sulfato_calcio=calcio-carbonato_calcio-bicarbonato_calcio

    if (bicarbonato-bicarbonato_calcio-bicarbonato_magnesio)>sodio: 
        bicarbonato_sodio=sodio
    else:
        bicarbonato_sodio=bicarbonato-bicarbonato_calcio-bicarbonato_magnesio

    if potasio>sulfatos-sulfato_calcio: 
        sulfato_potasio=sulfatos-sulfato_calcio
    else:
        sulfato_potasio=potasio

    if cloro>potasio-sulfato_potasio: 
        cloruro_potasio=potasio-sulfato_potasio
    else:
        cloruro_potasio=cloro

    if (sulfatos-sulfato_calcio-sulfato_potasio)>(magnesio-carbonato_magnesio-bicarbonato_magnesio): 

        sulfato_magnesio=magnesio-carbonato_magnesio-bicarbonato_magnesio
    else:
        sulfato_magnesio=sulfatos-sulfato_calcio-sulfato_potasio

    if (sodio-bicarbonato_sodio)>(cloro-cloruro_potasio): 
        cloruro_sodio=cloro-cloruro_potasio
    else:
        cloruro_sodio=sodio-bicarbonato_sodio

    if (sodio-bicarbonato_sodio-cloruro_sodio)>(sulfatos-sulfato_calcio-sulfato_potasio-sulfato_magnesio): 
        sulfato_sodio=sulfatos-sulfato_calcio-sulfato_potasio-sulfato_magnesio
    else:
        sulfato_sodio=sodio-bicarbonato_sodio-cloruro_sodio

    if (sodio-bicarbonato_sodio-cloruro_sodio-sulfato_sodio)>(carbonato-carbonato_calcio-carbonato_magnesio): 
        carbonato_sodio=carbonato-carbonato_calcio-carbonato_magnesio
    else:
        carbonato_sodio=sodio-bicarbonato_sodio-cloruro_sodio-sulfato_sodio
    
    if (magnesio-carbonato_magnesio-bicarbonato_magnesio-sulfato_magnesio)>(cloro-cloruro_potasio-cloruro_sodio): 
        cloruro_magnesio=cloro-cloruro_potasio-cloruro_sodio
    else:
        cloruro_magnesio=magnesio-carbonato_magnesio-bicarbonato_magnesio-sulfato_magnesio

    if (calcio-carbonato_calcio-bicarbonato_calcio-sulfato_calcio)>(cloro-cloruro_potasio-cloruro_sodio-cloruro_magnesio): 
        cloruro_calcio=cloro-cloruro_potasio-cloruro_sodio-cloruro_magnesio
    else:
        cloruro_calcio=calcio-carbonato_calcio-bicarbonato_calcio-sulfato_calcio


    #SOLUBILIDAD
    rango_1=carbonato_calcio+carbonato_magnesio+bicarbonato_magnesio+\
    sulfato_calcio+sulfato_potasio

    rango_2=bicarbonato_calcio+carbonato_sodio+bicarbonato_sodio+\
    sulfato_sodio+sulfato_magnesio+cloruro_potasio

    rango_3=cloruro_magnesio+cloruro_sodio+cloruro_calcio

    if rango_1>rango_2 and rango_1>rango_3:
        solubilidad= "<1000"
    elif rango_2>rango_1 and rango_2>rango_3:
        solubilidad= "1000-5000"
    else: 
        solubilidad=">5000"


    ####Sales 
    sales_list = [
        ("Carbonato de calcio:", carbonato_calcio),
        ("Carbonato de magnesio:", carbonato_magnesio),
        ("Bicarbonato de calcio:", bicarbonato_calcio),
        ("bicarbonato_magnesio", bicarbonato_magnesio),
        ("Sulfato de calcio", sulfato_calcio),
        ("bicarbonato_sodio", bicarbonato_sodio),
        ("Sulfato de potasio", sulfato_potasio),
        ("cloruro_potasio", cloruro_potasio),
        ("sulfato_magnesio", sulfato_magnesio),
        ("Cloruro de sodio", cloruro_sodio),
        ("sulfato_sodio", sulfato_sodio),
        ("carbonato_sodio", carbonato_sodio),
        ("cloruro_magnesio", cloruro_magnesio),
        ("cloruro_calcio", cloruro_calcio)
    ]

    # Ordenar la lista por valor en orden descendente.
    sorted_sales = sorted(sales_list, key=lambda x: x[1], reverse=True)

    # Obtener los 4 valores más altos.
    top_3_sales_inicial = sorted_sales[:4]

    # Crear una lista con los resultados formateados
    top_3_sales = [f"{nombre} {valor:.2f}" for nombre, valor in top_3_sales_inicial]
    

    #print(solubilidad)
    return carbonato_calcio, bicarbonato_calcio, carbonato_magnesio, bicarbonato_magnesio, solubilidad,top_3_sales




def actualizar_parametros(parametros, X):
    calcio = conversion(parametros["calcio"], 'calcio')
    magnesio = conversion(parametros["magnesio"], 'magnesio')
    carbonato = conversion(parametros["carbonato"], 'carbonato')
    bicarbonato = conversion(parametros["bicarbonato"], 'bicarbonato')

    calcio += X

    if calcio > carbonato:
        carbonato_calcio = carbonato
    else:
        carbonato_calcio = calcio

    if magnesio > (carbonato - carbonato_calcio):
        carbonato_magnesio = carbonato - carbonato_calcio
    else:
        carbonato_magnesio = magnesio

    if bicarbonato > calcio - carbonato_calcio:
        bicarbonato_calcio = calcio - carbonato_calcio
    else:
        bicarbonato_calcio = bicarbonato

    if (bicarbonato - bicarbonato_calcio) > (magnesio - carbonato_magnesio):
        bicarbonato_magnesio = magnesio - carbonato_magnesio
    else:
        bicarbonato_magnesio = bicarbonato - bicarbonato_calcio
    

    return {
        "calcio": calcio,
        "magnesio": magnesio,
        "sodio": conversion(parametros["sodio"], 'sodio'),
        "carbonato_calcio": carbonato_calcio,
        "bicarbonato_calcio": bicarbonato_calcio,
        "carbonato_magnesio": carbonato_magnesio,
        "bicarbonato_magnesio": bicarbonato_magnesio,
        "conductividad_electrica": parametros["conductividad_electrica"]
    }


def ras_modificado(parametros, X):
    params_actualizados = actualizar_parametros(parametros, X)
    
    calcio = params_actualizados["calcio"]
    magnesio = params_actualizados["magnesio"]
    sodio = params_actualizados["sodio"]
    carbonato_calcio = params_actualizados["carbonato_calcio"]
    bicarbonato_calcio = params_actualizados["bicarbonato_calcio"]
    carbonato_magnesio = params_actualizados["carbonato_magnesio"]
    bicarbonato_magnesio = params_actualizados["bicarbonato_magnesio"]

    numerador = sodio
    denominador = np.sqrt(
        (calcio - (carbonato_calcio + 0.5 * bicarbonato_calcio) + magnesio - (carbonato_magnesio + 0.25 * bicarbonato_magnesio)) / 2
    )

    return numerador / denominador

def ras_maximo(parametros, X):
    conductividad = parametros["conductividad_electrica"] + 0.1 * X
    return 8.689 * conductividad - 4.134

def ecuacion(X, parametros):
    return ras_modificado(parametros, X) - ras_maximo(parametros, X)

def encontrar_solucion(parametros):
    X_inicial = 0
    X_solucion = fsolve(ecuacion, X_inicial, args=(parametros))
    return X_solucion[0]

def condicion_sodicidad(parametros):
    X = 0
    ras_mod = ras_modificado(parametros, X)
    ras_max = ras_maximo(parametros, X)
    if ras_mod > ras_max:
        parametros["X_solucion"] = encontrar_solucion(parametros)
        #print(f"X_solucion calculado: {parametros['X_solucion']}")
        return parametros["X_solucion"]

    else:
        return "No hay perdida de infiltracion por sodio, por ende no se recomienda la aplicación de emiendas."


##############

def salinizacion_lavado (parametros): 
    
    conductividad_electrica = parametros["conductividad_electrica"]
    lluvia_total_anual = parametros["lluvia_total_anual"]
    tolerancia_cultivo = parametros["tolerancia_cultivo"]
    textura = parametros["textura"]

    evapotranspiracion = 9.142 - 0.004 * lluvia_total_anual
    requerimiento_riego = 365 * evapotranspiracion - 0.7 * lluvia_total_anual

    conductividad_electrica_ajustada = conductividad_electrica

    conductividad_electrica_infiltracion = (conductividad_electrica_ajustada * requerimiento_riego + 0.7 * 0.15 * lluvia_total_anual) / (requerimiento_riego + 0.7 * lluvia_total_anual)
    riego_lavado = conductividad_electrica_infiltracion / (3 * textura * tolerancia_cultivo)
    agua_extra = (riego_lavado / (1 - riego_lavado)) * 100
   
    return riego_lavado
    

def peligro_magnesio(parametros): 
    calcio = conversion(parametros["calcio"], 'calcio')
    magnesio = conversion(parametros["magnesio"], 'magnesio')

    mh = (magnesio*100)/(calcio+magnesio)
    print (f"peligro magnesio: {mh}")

    return mh    

""" 
def salinizacion_lavado (parametros): 
    
    if ras_modificado(parametros, 0) > ras_maximo(parametros, 0):
        X_solucion = encontrar_solucion(parametros)
        parametros["X_solucion"] = X_solucion
        print(f"X_solucion calculado: {X_solucion}")

        conductividad_electrica = parametros["conductividad_electrica"]
        lluvia_total_anual = parametros["lluvia_total_anual"]
        tolerancia_cultivo = parametros["tolerancia_cultivo"]
        textura = parametros["textura"]

        evapotranspiracion = 9.142 - 0.004 * lluvia_total_anual
        requerimiento_riego = 365 * evapotranspiracion - 0.7 * lluvia_total_anual

        if X_solucion > 0:
            conductividad_electrica_ajustada = conductividad_electrica + 0.1 * X_solucion
        else:
            conductividad_electrica_ajustada = conductividad_electrica

        conductividad_electrica_infiltracion = (conductividad_electrica_ajustada * requerimiento_riego + 0.7 * 0.15 * lluvia_total_anual) / (requerimiento_riego + 0.7 * lluvia_total_anual)
        riego_lavado = conductividad_electrica_infiltracion / (3 * textura * tolerancia_cultivo)
        agua_extra = (riego_lavado / (1 - riego_lavado)) * 100

        return riego_lavado
    else:
        conductividad_electrica = parametros["conductividad_electrica"]
        lluvia_total_anual = parametros["lluvia_total_anual"]
        tolerancia_cultivo = parametros["tolerancia_cultivo"]
        textura = parametros["textura"]

        evapotranspiracion = 9.142 - 0.004 * lluvia_total_anual
        requerimiento_riego = 365 * evapotranspiracion - 0.7 * lluvia_total_anual

        conductividad_electrica_ajustada = conductividad_electrica

        conductividad_electrica_infiltracion = (conductividad_electrica_ajustada * requerimiento_riego + 0.7 * 0.15 * lluvia_total_anual) / (requerimiento_riego + 0.7 * lluvia_total_anual)
        riego_lavado = conductividad_electrica_infiltracion / (3 * textura * tolerancia_cultivo)
        agua_extra = (riego_lavado / (1 - riego_lavado)) * 100

        return riego_lavado
 """




    
    



""" def ras_modificado(parametros):
    
    calcio = parametros["calcio"]
    magnesio = parametros["magnesio"]
    sodio = parametros["sodio"]
    carbonato_calcio = parametros["carbonato_calcio"]
    bicarbonato_calcio = parametros["bicarbonato_calcio"]
    carbonato_magnesio = parametros["carbonato_magnesio"]
    bicarbonato_magnesio = parametros["bicarbonato_magnesio"]

    ras_modificado=sodio/((calcio-(carbonato_calcio+0.5*bicarbonato_calcio)+magnesio-(carbonato_magnesio+0.25*bicarbonato_magnesio))/2)**(1/2)
    
    return ras_modificado

def ras_maximo(parametros):

    conductividad=parametros["conductividad_electrica"]

    ras_maximo=8.689*conductividad-4.134
    return ras_maximo """
    

#########SODIFICACION

"""
def actualizar_parametros(parametros, X):
    calcio = parametros["calcio"] + X
    magnesio = parametros["magnesio"]
    carbonato = parametros["carbonato"]
    bicarbonato = parametros["bicarbonato"]

    if calcio > carbonato: 
        carbonato_calcio = carbonato
    else:
        carbonato_calcio = calcio
    

    if magnesio > (carbonato - carbonato_calcio): 
        carbonato_magnesio = carbonato - carbonato_calcio
    else:
        carbonato_magnesio = magnesio
    
    if bicarbonato > calcio - carbonato_calcio: 
        bicarbonato_calcio = calcio - carbonato_calcio
    else:
        bicarbonato_calcio = bicarbonato

    if (bicarbonato - bicarbonato_calcio) > (magnesio - carbonato_magnesio): 
        bicarbonato_magnesio = magnesio - carbonato_magnesio
    else:
        bicarbonato_magnesio = bicarbonato - bicarbonato_calcio

    return {
        "calcio": calcio,
        "magnesio": magnesio,
        "sodio": parametros["sodio"],
        "carbonato_calcio": carbonato_calcio,
        "bicarbonato_calcio": bicarbonato_calcio,
        "carbonato_magnesio": carbonato_magnesio,
        "bicarbonato_magnesio": bicarbonato_magnesio,
        "conductividad_electrica": parametros["conductividad_electrica"]
    }

def ras_modificado(parametros, X):
    params_actualizados = actualizar_parametros(parametros, X)
    calcio = params_actualizados["calcio"]
    magnesio = params_actualizados["magnesio"]
    sodio = params_actualizados["sodio"]
    carbonato_calcio = params_actualizados["carbonato_calcio"]
    bicarbonato_calcio = params_actualizados["bicarbonato_calcio"]
    carbonato_magnesio = params_actualizados["carbonato_magnesio"]
    bicarbonato_magnesio = params_actualizados["bicarbonato_magnesio"]

    numerador = sodio
    denominador = np.sqrt(
        (calcio - (carbonato_calcio + 0.5 * bicarbonato_calcio) + magnesio - (carbonato_magnesio + 0.25 * bicarbonato_magnesio)) / 2
    )

    return numerador / denominador

def ras_maximo(parametros, X):
    conductividad = parametros["conductividad_electrica"] + 0.1 * X
    return 8.689 * conductividad - 4.134

def ecuacion(X, parametros):
    return ras_modificado(parametros, X) - ras_maximo(parametros, X)


 X_inicial = 0  # Valor inicial para la búsqueda
X_solucion = fsolve(ecuacion, X_inicial, args=(parametros))




 """
###################INTENTO
""" 
def actualizar_parametros(parametros, X):
    X=float(X)
    calcio = parametros["calcio"] + X
    magnesio = parametros["magnesio"]
    carbonato = parametros["carbonato"]
    bicarbonato = parametros["bicarbonato"]

    if calcio > carbonato: 
        carbonato_calcio = carbonato
    else:
        carbonato_calcio = calcio
    

    if magnesio > (carbonato - carbonato_calcio): 
        carbonato_magnesio = carbonato - carbonato_calcio
    else:
        carbonato_magnesio = magnesio
    
    if bicarbonato > calcio - carbonato_calcio: 
        bicarbonato_calcio = calcio - carbonato_calcio
    else:
        bicarbonato_calcio = bicarbonato

    if (bicarbonato - bicarbonato_calcio) > (magnesio - carbonato_magnesio): 
        bicarbonato_magnesio = magnesio - carbonato_magnesio
    else:
        bicarbonato_magnesio = bicarbonato - bicarbonato_calcio

    return {
        "calcio": calcio,
        "magnesio": magnesio,
        "sodio": parametros["sodio"],
        "carbonato_calcio": carbonato_calcio,
        "bicarbonato_calcio": bicarbonato_calcio,
        "carbonato_magnesio": carbonato_magnesio,
        "bicarbonato_magnesio": bicarbonato_magnesio,
        "conductividad_electrica": parametros["conductividad_electrica"]
    }

def ras_modificado(parametros, X):
    params_actualizados = actualizar_parametros(parametros, X)
    calcio = params_actualizados["calcio"]
    magnesio = params_actualizados["magnesio"]
    sodio = params_actualizados["sodio"]
    carbonato_calcio = params_actualizados["carbonato_calcio"]
    bicarbonato_calcio = params_actualizados["bicarbonato_calcio"]
    carbonato_magnesio = params_actualizados["carbonato_magnesio"]
    bicarbonato_magnesio = params_actualizados["bicarbonato_magnesio"]

    numerador = sodio
    denominador = np.sqrt(
        (calcio - (carbonato_calcio + 0.5 * bicarbonato_calcio) + magnesio - (carbonato_magnesio + 0.25 * bicarbonato_magnesio)) / 2
    )
    
    
    return numerador / denominador
    

def ras_maximo(parametros, X):
    conductividad = parametros["conductividad_electrica"] + 0.1 * X
    return 8.689 * conductividad - 4.134

def ecuacion(X, parametros):
    return ras_modificado(parametros, X) - ras_maximo(parametros, X)

def encontrar_solucion(parametros):
    X_inicial = 0  # Valor inicial para la búsqueda
    X_solucion = fsolve(ecuacion, X_inicial, args=(parametros))
    print(X_solucion)
    
    return X_solucion[0]
    


def condicion_sodicidad(parametros):
    X = 0  # Puedes ajustar este valor según sea necesario
    ras_mod = ras_modificado(parametros, X)
    ras_max = ras_maximo(parametros, X)

    if ras_mod > ras_max:        
        X_solucion_nueva=encontrar_solucion(parametros)
        parametros["X_solucion"] = X_solucion_nueva

        #print(f"X_solucion calculado: {parametros['X_solucion']}")
        print(X_solucion_nueva)
        return X_solucion_nueva
    
    else:
        return "No hay perdida de infiltracion por sodio, por ende no se recomienda la aplicación de emiendas." """


