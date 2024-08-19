from django.db import models
""" 
python manage.py makemigrations
python manage.py migrations """

class AfectacionGeneral(models.Model):
    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_afectacion = models.TextField(blank=True, null=True)
    recomendacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nivel_afectacion} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion}"
    
    @staticmethod
    def obtener_afectacion(valor: float) -> "AfectacionGeneral":
        
        try:
            afectacion = AfectacionGeneral.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            
            return None

class AfectacionDetalladaInfraestructura(models.Model):
    nombre = models.TextField(blank=True, null=True)
    parametro = models.TextField(blank=True, null=True)
    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_afectacion = models.TextField(blank=True, null=True)
    posible_peligro = models.TextField(blank=True, null=True)
    recomendacion_fisica = models.TextField(blank=True, null=True)
    recomendacion_quimica = models.TextField(blank=True, null=True)
    recomendacion_biologica = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.parametro}-{self.nivel_afectacion} - {self.posible_peligro} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion_fisica} - {self.recomendacion_quimica} - {self.recomendacion_biologica}"
    
    @staticmethod
    def obtener_afectacion_infraestructura(parametro:str,valor: float) -> "AfectacionDetalladaInfraestructura":
        
        try:
            afectacion = AfectacionDetalladaInfraestructura.objects.filter(parametro=parametro,valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            
            return None

class AfectacionDetalladaIncrustracion(models.Model):
    nombre = models.TextField(blank=True, null=True)
    parametro = models.TextField(blank=True, null=True)
    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_peligro = models.TextField(blank=True, null=True)
    posible_peligro = models.TextField(blank=True, null=True)
    recomendacion_fisica = models.TextField(blank=True, null=True)
    recomendacion_quimica = models.TextField(blank=True, null=True)
    recomendacion_biologica = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.parametro}-{self.nivel_peligro} - {self.posible_peligro} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion_fisica} - {self.recomendacion_quimica} - {self.recomendacion_biologica}"
    
    @staticmethod
    def obtener_afectacion_incrustracion(parametro:str,valor: float) -> "AfectacionDetalladaIncrustracion":
        
        try:
            afectacion_incrustracion = AfectacionDetalladaIncrustracion.objects.filter(parametro=parametro,valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion_incrustracion
        except Exception as e:
            
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
        
        try:
            afectacion = SueloGeneral.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            
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
        
        try:
            afectacion = SueloGeneral.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            
            return None
        
class SueloSalinizacion(models.Model):
    conductividad_electrica = models.FloatField(blank=True, null=True)
    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    solubilidad = models.TextField(blank=True, null=True)
    nivel_afectacion = models.TextField(blank=True, null=True)
    posible_afectacion = models.TextField(blank=True, null=True)
    recomendacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.conductividad_electrica} - {self.valor_minimo} - {self.valor_maximo} -\
            - {self.solubilidad} - {self.nivel_afectacion}-{self.posible_afectacion} - {self.recomendacion}"
    
    @staticmethod
    def suelo_salinizacion(solubilidad: str, valor: float) -> "SueloSalinizacion":
        
        try:
            afectacion = SueloSalinizacion.objects.filter(solubilidad=solubilidad, valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return afectacion
        except Exception as e:
            
            return None

"""         
class RasOriginal(models.Model):
    hco3_ca = models.FloatField()
    conductividad_electrica = models.FloatField()
    valor = models.FloatField()

    @staticmethod
    def __str__(self):
        return f"HCO3/Ca: {self.hco3_ca}, CE: {self.ce}, Valor: {self.valor}" """

class Sodificacion(models.Model):

    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_peligro = models.TextField(blank=True, null=True)
    recomendacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nivel_peligro} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion}"
    
    @staticmethod
    def sodificacion(valor: float) -> "Sodificacion":
        
        try:
            sodificacion = Sodificacion.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return sodificacion
        except Exception as e:
            
            return None
        
class Salinizacion(models.Model):

    valor_minimo = models.FloatField(blank=True, null=True)
    valor_maximo = models.FloatField(blank=True, null=True)
    nivel_peligro = models.TextField(blank=True, null=True)
    recomendacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nivel_peligro} - {self.valor_minimo} - {self.valor_maximo} - {self.recomendacion}"
    
    @staticmethod
    def salinizacion(valor: float) -> "Salinizacion":
        
        try:
            salinizacion = Salinizacion.objects.filter(valor_minimo__lt=valor, valor_maximo__gte=valor).first()
            return salinizacion
        except Exception as e:
            
            return None