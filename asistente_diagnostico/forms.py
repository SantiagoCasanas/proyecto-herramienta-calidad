# affectation/forms.py
from django import forms

class AfectacionGeneralForm(forms.Form):
    valor = forms.IntegerField(label='Valor de referencia', min_value=0)

    choices_t = (("superficial", "superficial"), ("subterraneo", "subterraneo"))
    valor1 = forms.ChoiceField(choices=choices_t, label='texto de referencia')
