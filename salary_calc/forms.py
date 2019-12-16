from django import forms

class SalaryForm(forms.Form):
    param1 = forms.IntegerField(label='1 - Wynagrodzenie brutto', min_value=1500)
    param2 = forms.IntegerField(label='2 - Wynagrodzenie brutto', min_value=1500)
    param3 = forms.IntegerField(label='3 - Wynagrodzenie brutto', min_value=1500)
    param4 = forms.IntegerField(label='4 - Wynagrodzenie brutto', min_value=1500)
    param5 = forms.IntegerField(label='5 - Wynagrodzenie brutto', min_value=1500)
    param6 = forms.IntegerField(label='6 - Wynagrodzenie brutto', min_value=1500)