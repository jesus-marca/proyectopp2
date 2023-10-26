from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo
from .models import UserProfileInfo

#formulario user
class UserForm(UserCreationForm):
    email = forms.EmailField(label="correo electronico")

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

        labels = {
        'username':"Nombre de usuario",
        'first_name':"Nombre",
        'last_name':"Apellidos",      
        'password1':'Password',
        'password2':'Confirm Password'
        }

# formulario actualizar user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="correo electronico")

    class Meta():
        model = User
        fields = ['username','first_name','last_name', 'email']

        labels = {
        'username':"Nombre de usuario",
        'first_name':"Nombre",
        'last_name':"Apellidos",      
        }

#Formulario perfil usuario
class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(label="Detalles",required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'estudiante'),
        (teacher, 'profesor'),
    ]
    user_type = forms.ChoiceField(label="Tipo de estudiante",required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio','user_type')
        labels={
            # 'bio':'tipo'
        }
#Formulario actualizar perfil usuario
class UserProfileUpdateInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('bio','profile_pic','user_type')
        labels={
            'bio':'tipo'
        }