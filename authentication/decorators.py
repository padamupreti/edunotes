from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from django.conf import settings


def redirect_authenticated(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:home')
        return func(request, *args, **kwargs)

    return inner


def login_required_htmx(func):
    def inner(request, *args, **kwargs):
        if request.user.is_anonymous:
            response = HttpResponse()
            response.headers['HX-Redirect'] = reverse(settings.LOGIN_URL)
            return response
        return func(request, *args, **kwargs)

    return inner
