from django import forms
from django import models

class SearchModelForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = ['username','first_name', 'last_name']