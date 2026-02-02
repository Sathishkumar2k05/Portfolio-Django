from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['name', 'email', 'message']

        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder':'Enter your name', 
                'style':'padding:10px; width:300px; border-left: 5px solid #38bdf8; margin-bottom:10px;'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control', 
                'placeholder':'Enter your email', 'style':' padding:10px; width:300px; border-left: 5px solid #38bdf8; margin-bottom:10px;'
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control', 
                'placeholder':'Enter your message',
                'style':'width:300px; padding:10px; border-left: 5px solid #38bdf8; margin-bottom: 10px;'
            })
        }