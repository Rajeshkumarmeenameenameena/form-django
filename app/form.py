from django import forms
class studentform(forms.Form):
    name=forms.CharField(max_length=20,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))