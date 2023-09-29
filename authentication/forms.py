from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        email.strip()
        same_mail_users = User.objects.filter(email=email)
        if same_mail_users:
            raise ValidationError('A user with that email already exists.')
        return email

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user
