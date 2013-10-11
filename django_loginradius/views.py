from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponseRedirect
import logging

@csrf_exempt
def connect(request):
    lr_token=request.POST.get('token', False)
    user = authenticate(token=lr_token)
    login(request, user)
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
