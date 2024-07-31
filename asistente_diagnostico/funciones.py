
import numpy as np
from scipy.optimize import fsolve
#from .models import *
from .models import AfectacionDetalladaInfraestructura

#Activamos el ambiente: source venv/Scripts/activate
#Corremos el proyecto: python manage.py runserver

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
    

def inidice_langelier(parametros):

    ph = parametros["ph"]
    temperatura = parametros["temperatura"]
    alcalinidad = parametros["alcalinidad"]
    dureza = parametros["dureza"]

    indice_langelier = temperatura+ph+alcalinidad+dureza-12.5
    
    return indice_langelier

#SUELO

#######indice o tabla 1

def ras_original (parametros):
    magnesio = parametros["magnesio"]
    sodio = parametros["sodio"]
    calcio= parametros ["calcio"]
    bicarbonato = parametros["bicarbonato"]

    pass


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
    

def sales (parametros):

    calcio = parametros["calcio"]
    magnesio = parametros["magnesio"]
    sodio = parametros["sodio"]
    potasio = parametros["potasio"]
    carbonato = parametros["carbonato"]
    bicarbonato = parametros["bicarbonato"]
    cloro = parametros["cloro"]
    sulfatos = parametros["sulfatos"]

    if calcio>carbonato: 
        carbonato_calcio=carbonato
    else:
        carbonato_calcio=calcio
    print("carbonato_calcio:", carbonato_calcio)

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
    
    return carbonato_calcio, bicarbonato_calcio, carbonato_magnesio, bicarbonato_magnesio


def ras_modificado(parametros):
    
    calcio = parametros["calcio"]
    magnesio = parametros["magnesio"]
    sodio = parametros["sodio"]
    carbonato_calcio = parametros["carbonato_calcio"]
    bicarbonato_calcio = parametros["bicarbonato_calcio"]
    carbonato_magnesio = parametros["carbonato_magnesio"]
    bicarbonato_magnesio = parametros["bicarbonato_magnesio"]

    ras_modificado=sodio/((calcio-(carbonato_calcio+0.5*bicarbonato_calcio)+magnesio-(carbonato_magnesio+0.25*bicarbonato_magnesio))/2)**(1/2)
    print(ras_modificado)
    return ras_modificado

def ras_maximo(parametros):

    conductividad=parametros["conductividad_electrica"]

    ras_maximo=8.689*conductividad-4.134
    return ras_maximo
    

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
    print("carbonato_calcio:", carbonato_calcio)

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

print(f"El valor mínimo de X para que ras_maximo y ras_modificado sean iguales es: {X_solucion[0]}")

 """
def calcular_valor_x(parametros):
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
    
    return X_solucion[0]



    
    


