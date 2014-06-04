from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    company = forms.CharField()
    title = forms.CharField()
    phone_number = forms.CharField()
    email =  forms.EmailField()
    message = forms.TextField(required=False)


