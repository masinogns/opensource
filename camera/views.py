from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'camera/index.html'

class SituationView(TemplateView):
    template_name = 'camera/situation.html'

class DifferentView(TemplateView):
    template_name = 'camera/different.html'

class PreventView(TemplateView):
    template_name = 'camera/prevent.html'
