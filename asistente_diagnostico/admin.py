from django.contrib import admin

from asistente_diagnostico.models import *

# Register your models here.
admin.site.register(AfectacionGeneral)
admin.site.register(AfectacionDetalladaInfraestructura)
admin.site.register(SueloGeneral)
admin.site.register(SueloSalinizacion)
admin.site.register(Salinizacion)
admin.site.register(Sodificacion)
admin.site.register(AfectacionDetalladaIncrustracion)
admin.site.register(SalinizacionFao)