from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo

class UserForm(UserCreationForm):
    email = forms.EmailField(label="correo electronico")

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        # }
        labels = {
        'username':"Nombre de usuario",
        'first_name':"Nombre",
        'last_name':"Apellidos",      
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(label="Detalles",required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'estudiante'),
        (parent, 'apoderado'),
    ]
    user_type = forms.ChoiceField(label="Tipo de estudiante",required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio','profile_pic','user_type')
        labels={
            'bio':'tipo'
        }

