from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

#extiende el formulario UserCreationForm para que contenga el campo Email
#Asimismo, valida el contenido del Email ingresado
class UserCreationformWithEmail(UserCreationForm):
    email = forms.EmailField (required=True, help_text= "Ingrese su Email. 254 caracteres como máximo y deben ser valido")

    class Meta:
        model = User
        fields = ('username','password1','password2','email')
    
    #permite validar la existencia de Emails duplicados
    def clean_email(self):
        email = self.cleaned_data.get("email")#recupera el campo que vamos a validar
        if User.objects.filter(email=email).exists():#compara la existencia de Emails duplicados
            raise forms.ValidationError("Ya existen usuarios registrados con este Email, ingrese otro")
        return email

#formulario para ingreso de datos al perfil
class ProfileForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio':forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link':forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }
#permite editar el email
class EmailForm(forms.ModelForm):
    email = forms.EmailField (required=True, help_text= "Ingrese su Email. 254 caracteres como máximo y deben ser valido")
    
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")#recupera el campo que vamos a validar
        if 'email' in self.changed_data:#compruba si ya hay un mail guardado y si se modificó
            if User.objects.filter(email=email).exists():#compara la existencia de Emails duplicados
                raise forms.ValidationError("Ya existen usuarios registrados con este Email, ingrese otro")
        return email
