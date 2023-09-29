from django.shortcuts import redirect


def redirect_authenticated(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('summarizer:home')
        return func(request, *args, **kwargs)

    return inner
