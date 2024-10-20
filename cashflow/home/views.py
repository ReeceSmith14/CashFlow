from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def custom_login_redirect(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    return redirect('/dashboard/')


