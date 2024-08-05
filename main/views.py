from django.shortcuts import render
from django.utils.translation import gettext as _

def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def donate(request):
    return render(request, 'main/donate.html')