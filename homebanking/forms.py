from django import forms

class EditForm(forms.Form):

    CHOICES = (('CLASSIC', 'CLASSIC'), ('GOLD', 'GOLD'), ('BLACK', 'BLACK'))

    cliente_id= forms.CharField(label="cliente_id", required= True)
    pwd = forms.CharField(label= "pwd", required= True)
    tipo_cliente = forms.ChoiceField(label="tipo_cliente", required= True, choices= CHOICES)
    dob = forms.DateField(label= "dob", required= True)
    email = forms.CharField(label="email", required= True)
    img_profile = forms.ImageField(label="img_profile", required= False)