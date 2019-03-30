from django import forms
from django.core.validators import MinValueValidator, MinLengthValidator

class OriginForm(forms.Form):
    origin_address = forms.CharField(validators=[MinLengthValidator(1)],
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'id': 'inlineFormInputGroup',
                                                                   'placeholder': '123 Tech St, Silicon Valley, CA 00000'}))

class DestinationForm(forms.Form):
    destination_address = forms.CharField(validators=[MinLengthValidator(1)],
                                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'id': 'inlineFormInputGroup',
                                                                        'placeholder': '123 Tech St, Silicon Valley, CA 00000'}))

class GasPriceForm(forms.Form):
    gas_price = forms.FloatField(validators=[MinValueValidator(0.01)],
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'id': 'inlineFormInputGroup',
                                                               'placeholder': '1.23'}))

class MpgForm(forms.Form):
    mpg = forms.FloatField(validators=[MinValueValidator(0.01)],
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'id': 'inlineFormInputGroup',
                                                         'placeholder': '12'}))

class NumPeopleForm(forms.Form):
    num_people = forms.IntegerField(validators=[MinValueValidator(1)],
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'id': 'inlineFormInputGroup',
                                                                  'placeholder': '1 (default is 1 if left blank)'}))
