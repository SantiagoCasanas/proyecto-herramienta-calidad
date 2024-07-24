from .models import *

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
    



