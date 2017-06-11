from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

def IndexView(request):
    return render(request, 'introduce/index.html')
