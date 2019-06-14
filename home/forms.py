from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=120, widget=forms.TextInput(attrs={'id':'form_name','class':'form-control', 'placeholder':'Enter Name', 'required':'required'}))

    email = forms.EmailField(label='', max_length=120, widget=forms.TextInput(attrs={'id':'form_email','class':'form-control', 'placeholder':'Enter Email', 'required':'required'}))

    subject = forms.CharField(label='', max_length=120, widget=forms.TextInput(attrs={'id':'form_subject','class':'form-control', 'placeholder':'Enter Subject', 'required':'required'}))

    phone = forms.CharField(label='', max_length=12, widget=forms.TextInput(attrs={'id':'form_phone','class':'form-control', 'placeholder':'Enter Phone', 'required':'required'}))

    
    
    message = forms.CharField(label='', max_length=120, widget=forms.Textarea(attrs={'id':'form_message','class':'form-control', 'placeholder':'Enter Message', 'required':'required', 'rows':5}))

   