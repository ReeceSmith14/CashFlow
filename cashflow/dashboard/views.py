from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.helpers import complete_social_login
from django.http import JsonResponse

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')




def google_login_by_token(request):
    # Process the token here and authenticate the user
    token = request.POST.get('credential')