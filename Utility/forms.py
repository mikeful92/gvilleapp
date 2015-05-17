from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label="Street Address", max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))