from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
       model = CustomUsuario
       fields = ['username', 'first_name', 'last_name']
       labels = {'username': 'Username/E-mail'}

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = CustomUsuario.objects.filter(username=username)
        if r.count():
            raise ValidationError("Usuário já existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = CustomUsuario.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email já existe")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Senhas não correspondem")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = {'first_name', 'last_name'}
