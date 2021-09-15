 
from django.forms.models import ModelForm
from .models import gadgets
from django.forms import TextInput

class gadgetForm(ModelForm):

    class Meta:
        model = gadgets
        fields= ['Name','Image','Year','Price']

        widgets = { 

            'Name' : TextInput(attrs={'class':'form-control',
                            'style': 'max-width: 300px;',
                            'placeholder':'Gadget Name'
                            }),
            'Year' : TextInput(attrs={'class':'form-control',
                            'style': 'max-width: 300px;',
                            'placeholder':'Mfg.Year'
                            }),
            'Price': TextInput(attrs={'class':'form-control',
                            'style': 'max-width: 300px;',
                            'placeholder':'Price'
                            })
        }