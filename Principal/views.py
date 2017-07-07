from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext #as _
# Create your views here.

def index(request):
    # Translators: This message appears on the home page only
    output = ugettext("Welcome to my site.")
    return HttpResponse(output)