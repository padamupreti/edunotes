from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .decorators import redirect_authenticated
from .forms import EmailUserCreationForm


@redirect_authenticated
def login_or_register(request):
    login_form = AuthenticationForm()
    sign_up_form = EmailUserCreationForm()
    redirect_url = request.GET.get('next') or 'summarizer:home'

    post_data = request.POST
    if post_data:
        if post_data['form_type'] == 'login_form':
            # del post_data['form_type']
            login_form = AuthenticationForm(data=post_data)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(redirect_url)
        elif post_data['form_type'] == 'sign_up_form':
            # del post_data['form_type']
            sign_up_form = EmailUserCreationForm(post_data)
            if sign_up_form.is_valid():
                user = sign_up_form.save()
                login(request, user)
                return redirect(redirect_url)

    context = {
        'login_form': login_form,
        'sign_up_form': sign_up_form,
    }

    return render(request, 'authentication/login-or-register.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('summarizer:home')
