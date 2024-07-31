# affectation/forms.py
from django import forms

class AfectacionGeneralForm(forms.Form):
    
    choices_t = (("superficial", "superficial"), ("subterranea", "subterranea"))
    fuentes_abastecimiento = forms.ChoiceField(choices=choices_t, label='Fuente de abastecimiento')
    ph = forms.FloatField(label='pH:', min_value=0)
    conductividad_electrica = forms.FloatField(label='Conductividad electrica [CEw]', min_value=0)
    calcio = forms.FloatField(label='Calcio [Ca]:', min_value=0)
    sodio = forms.FloatField(label='Sodio [Na]:', min_value=0)
    magnesio = forms.FloatField(label='Mangnesio [Mg]', min_value=0)
    potasio = forms.FloatField(label='Potasio [K]:', min_value=0)
    carbonato = forms.FloatField(label='Carbonato [CO3--]:', min_value=0)
    bicarbonato = forms.FloatField(label='Bicarbonato [HCO3-]:', min_value=0)
    cloro = forms.FloatField(label='Cloro [Cl-]:', min_value=0)
    
    solidos_disueltos = forms.FloatField(label='Solidos disueltos [SD]', min_value=0)
    solidos_solubles = forms.FloatField(label='Solidos solubles totales [SST]', min_value=0)
    hierro = forms.FloatField(label='Hierro [Fe]', min_value=0)
    manganeso = forms.FloatField(label='Manganeso [Mn]', min_value=0)
    
    nitrogeno = forms.FloatField(label='Nitrógeno total', min_value=0)
    amonio = forms.FloatField(label='Amonio [NH4]', min_value=0)
    sulfatos = forms.FloatField(label='Sulfatos [SO4-2]', min_value=0)
    temperatura = forms.FloatField(label='Temperatura', min_value=0)
    alcalinidad = forms.FloatField(label='Alcalinidad', min_value=0)
    dureza = forms.FloatField(label='Dureza', min_value=0)

    carbonato_sodico_residual= forms.FloatField(label='Carbonato Sodico Residual [CSR]', min_value=0)
    porcentaje_sodio_soluble= forms.FloatField(label='Porcenstaje de sodio soluble [%PSS]', min_value=0)