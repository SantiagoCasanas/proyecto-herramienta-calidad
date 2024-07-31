from django.db import models

class AfectacionGeneral(models.Model):
    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_afectacion = models.TextField(blank=True, null=True)
    recomendacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nivel_afectacion} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion}"
    
    @staticmethod
    def obtener_afectacion(valor: float) -> "AfectacionGeneral":
        print("------")
        try:
            afectacion = AfectacionGeneral.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            print(e)
            return None

class AfectacionDetalladaInfraestructura(models.Model):
    parametro = models.TextField(blank=True, null=True)
    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_afectacion = models.TextField(blank=True, null=True)
    recomendacion_fisica = models.TextField(blank=True, null=True)
    recomendacion_quimica = models.TextField(blank=True, null=True)
    recomendacion_biologica = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.parametro}-{self.nivel_afectacion} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion_fisica} - {self.recomendacion_quimica} - {self.recomendacion_biologica}"
    
    @staticmethod
    def obtener_afectacion_infraestructura(parametro:str,valor: float) -> "AfectacionDetalladaInfraestructura":
        print("------")
        try:
            afectacion = AfectacionDetalladaInfraestructura.objects.filter(parametro=parametro,valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            print(e)
            return None

class SueloGeneral(models.Model):

    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_afectacion = models.TextField(blank=True, null=True)
    recomendacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nivel_afectacion} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion}"
    
    @staticmethod
    def obtener_suelo_general(valor: float) -> "SueloGeneral":
        print("------")
        try:
            afectacion = SueloGeneral.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            print(e)
            return None
"""         
class RasOriginal(models.Model):
    hco3_ca = models.FloatField()
    conductividad_electrica = models.FloatField()
    valor = models.FloatField()

    @staticmethod
    def __str__(self):
        return f"HCO3/Ca: {self.hco3_ca}, CE: {self.ce}, Valor: {self.valor}" """