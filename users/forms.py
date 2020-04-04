from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            'class': 'input pass',
            'placeholder' : "What's your email?",
            'name' : 'user[email]'
        }))
    username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'input pass',
            'placeholder' : "What's your username?",
            'name' : 'user[name]'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'input pass',
            'placeholder' : "What's your first name?",
            'name' : 'user[name]'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'input pass',
            'placeholder' : "What's your last name?",
            'name' : 'user[name]'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'input pass',
            'placeholder' : "Choose a password",
            'name' : 'user[password1]'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'input pass',
            'placeholder' : "Confirm password",
            'name' : 'user[password2]'
        }
    ))
    
    class Meta:
        model = User
        fields = ('username',
         'first_name',
         'last_name',
         'email',
         'password1',
         'password2'
         )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class LoginForm(forms.ModelForm):
    
    class Meta(forms.ModelForm):
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'maxlength': 250}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'maxlength': 250}),
        }