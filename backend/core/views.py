from django.shortcuts import render
from django.shortcuts import redirect

def root_redirect(request):
    return render(request, 'core/register.html')  # replace 'some_named_url' with the actual URL name or path


def profile_view(request):
    return render(request, 'core/profile.html')

def dashboard_view(request):
    return render(request, 'core/dashboard.html')

def register_page(request):
    return render(request, 'core/register.html')

def login_page(request):
    return render(request, 'core/login.html')
