# affectation/forms.py
from django import forms


class AfectacionGeneralForm(forms.Form):
    
    usuario = forms.CharField(
        label='Usuario', 
        widget=forms.TextInput(attrs={'class': 'input-color'}),  
    )

    choices_t = (("superficial", "superficial"), ("subterranea", "subterranea"))

    fuentes_abastecimiento = forms.ChoiceField(
        choices=choices_t, 
        label='Fuente de abastecimiento',
        widget=forms.Select(attrs={'class': 'input-color'}),
        
    )    

    nombre_fuente = forms.CharField(
        label='Nombre de la fuente', 
        widget=forms.TextInput(attrs={'class': 'input-color'}),  
    )

    lugar = forms.CharField(
        label='País/Departamento', 
        widget=forms.TextInput(attrs={'class': 'input-color'}),  
    )

    laboratorio = forms.CharField(
        label='Laboratorio', 
        widget=forms.TextInput(attrs={'class': 'input-color'}),  
    )

    fecha_muestreo = forms.CharField(
        label='Fecha de muestreo', 
        widget=forms.TextInput(attrs={'class': 'input-color'}),  
    )

    choices_riego = (("Gravedad", "Gravedad"), ("Goteo", "Goteo"), ("Aspersión", "Aspersión"))

    metodo_riego = forms.ChoiceField(
        choices=choices_riego, 
        label='Método de riego',
        widget=forms.Select(attrs={'class': 'input-color'}),
        
    )  

    ph = forms.FloatField(
        label='pH:', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )

    conductividad_electrica = forms.FloatField(
        label='Conductividad electrica (CEw) [dS m-1]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
       
    )

    calcio = forms.FloatField(
        label='Calcio (Ca) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )   

    sodio = forms.FloatField(
        label='Sodio (Na) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )   
    
    magnesio = forms.FloatField(
        label='Magnesio (Mg) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )   
    
    potasio = forms.FloatField(
        label='Potasio (K) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )  

    carbonato = forms.FloatField(
        label='Carbonato (CO3--) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )  

    bicarbonato = forms.FloatField(
        label='Bicarbonato (HCO3-) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
       
    )  

    cloro = forms.FloatField(
        label='Cloro (Cl-) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )  
    
    sulfatos = forms.FloatField(
        label='Sulfatos (SO4-2) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
       
    ) 

    solidos_disueltos = forms.FloatField(
        label='Solidos disueltos (SD) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )     
    solidos_solubles = forms.FloatField(
        label='Solidos suspendidos totales (SST) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
       
    ) 
    
    hierro = forms.FloatField(
        label='Hierro (Fe) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    ) 
    
    manganeso = forms.FloatField(
        label='Manganeso [Mn] [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )
    
    nitrogeno = forms.FloatField(
        label='Nitrógeno total (N) [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )

    amonio = forms.FloatField(
        label='Amonio [NH4] [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )
    
    temperatura = forms.FloatField(
        label='Temperatura [°C]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
       
    )
    
    alcalinidad = forms.FloatField(
        label='Alcalinidad [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )
 
    dureza = forms.FloatField(
        label='Dureza [mg/L]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )
    
    lluvia_total_anual = forms.FloatField(
        label='Lluvia total anual [mm]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )

    textura = forms.FloatField(
        label='Eficiencia de lavado según la textura [Arcilloso=0.5, Franco=0.7, Arenoso=0.9]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )

    tolerancia_cultivo = forms.FloatField(
        label='Tolerancia del cultivo a la sales [dS m-1]', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'input-color'}),
        
    )