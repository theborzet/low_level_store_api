from django import forms

class NewGoodForm(forms.Form):
    name = forms.CharField(max_length=100)
    amount = forms.IntegerField()
    price = forms.DecimalField(min_value=0)