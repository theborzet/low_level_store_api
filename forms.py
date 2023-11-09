from django import forms

class NewGoodForm(forms.Form):
    name = forms.CharField(max_length=100)
    amount = forms.IntegerField(min_value=0)
    price = forms.FloatField(min_value=0)