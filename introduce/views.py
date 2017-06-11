from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'introduce/index.html'

class StoryView(TemplateView):
    template_name = 'introduce/story.html'

class EffectView(TemplateView):
    template_name = 'introduce/effect.html'

class FutureView(TemplateView):
    template_name = 'introduce/future.html'
