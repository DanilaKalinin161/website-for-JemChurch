from django.shortcuts import render
from django.utils.translation import gettext as _
from main.models import Slider

def index(request):
    context = Slider.objects.order_by('name')[:1]
    slider_bd_two = Slider.objects.order_by('name')[:2]

    return render(request, 'main/index.html', {'context': context, 'slider_bd_two': slider_bd_two})
def about(request):
    return render(request, 'main/about.html')
def donate(request):
    return render(request, 'main/donate.html')