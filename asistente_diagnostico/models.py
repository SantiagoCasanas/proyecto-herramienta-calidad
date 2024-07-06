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