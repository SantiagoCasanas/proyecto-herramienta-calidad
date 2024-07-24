# affectation/forms.py
from django import forms

class AfectacionGeneralForm(forms.Form):
    
    choices_t = (("superficial", "superficial"), ("subterranea", "subterranea"))
    fuentes_abastecimiento = forms.ChoiceField(choices=choices_t, label='Fuente de abastecimiento')
    conductividad_electrica = forms.IntegerField(label='Conductividad electrica', min_value=0)
    ph = forms.IntegerField(label='pH:', min_value=0)
    solidos_disueltos = forms.IntegerField(label='Solidos disueltos', min_value=0)
    solidos_solubles = forms.IntegerField(label='Solidos solubles totales', min_value=0)
    hierro = forms.IntegerField(label='Hierro [Fe]', min_value=0)
    manganeso = forms.IntegerField(label='Manganeso [Mn]', min_value=0)
    magnesio = forms.IntegerField(label='Mangnesio [Mg]', min_value=0)
    nitrogeno = forms.IntegerField(label='Nitrógeno total', min_value=0)
    amonio = forms.IntegerField(label='Amonio [NH4]', min_value=0)
    sulfatos = forms.IntegerField(label='Sulfatos [SO4-2]', min_value=0)
    temperatura = forms.IntegerField(label='Temperatura', min_value=0)
    alcalinidad = forms.IntegerField(label='Alcalinidad', min_value=0)
    dureza = forms.IntegerField(label='Dureza', min_value=0)
   