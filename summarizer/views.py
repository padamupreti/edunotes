from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'summarizer/home.html', context={})


@login_required
def create_summary(request):
    return render(request, 'summarizer/create-summary.html', context={})


@login_required
def list_summaries(request):
    return redirect('summarizer:create-summary')
