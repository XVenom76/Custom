from django import forms

class Registration_form(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.TextField()
    url = forms.CharField(max_length=100)
#this should be used to store the data from register template
