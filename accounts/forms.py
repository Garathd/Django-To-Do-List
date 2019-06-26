from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models import UserProfile

# UserProfile form which lets users update there profile
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['description', 'picture']
        widgets = {
            'description': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Please enter a profile description'
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class':'btn btn-default auto-width'
            }),
        }
        
# UserLogin form which lets users log in to the website
class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(label="Enter a Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter a Password")

# UserRegistration form which lets users log in to the website
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
