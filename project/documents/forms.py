# coding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class DocumentForm(forms.Form):

    class Meta:
        fields = ('texto')
    texto = forms.CharField(label=_("Texto a traducir"), required=True, widget=forms.Textarea(attrs={'class': 'materialize-textarea', 'data-length': '300'}))

    