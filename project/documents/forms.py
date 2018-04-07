# coding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class DocumentForm(forms.Form):

    class Meta:
        fields = ('date', 'name', 'last_name', 'occupation',
                  'age', 'product', 'units', 'zone')
    date = forms.CharField(label=_("Fecha"), required=True,
                           widget=forms.TextInput(attrs={'class': 'datepicker validate'}))
    name = forms.CharField(label=_("Nombre"), required=True,
                           widget=forms.TextInput(attrs={'class': 'validate'}))
    last_name = forms.CharField(label=_(
        "Apellido"), required=True, widget=forms.TextInput(attrs={'class': 'validate'}))
    occupation = forms.CharField(label=_("Ocupación"), required=True,
                                 widget=forms.TextInput(attrs={'class': 'validate'}))
    age = forms.IntegerField(label=_("Edad"), required=True,
                             widget=forms.TextInput(attrs={'class': 'validate'}))
    product = forms.CharField(label=_("Producto"), required=True,
                              widget=forms.TextInput(attrs={'class': 'validate'}))
    units = forms.IntegerField(label=_("Unidades"), required=True,
                               widget=forms.TextInput(attrs={'class': 'validate'}))
    zone = forms.CharField(label=_("Zona"), required=True,
                           widget=forms.TextInput(attrs={'class': 'validate'}))
