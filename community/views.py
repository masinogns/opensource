from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from community.models import Community

class IndexView(TemplateView):
    template_name = 'community/index.html'

class CommunityList(ListView):
    model = Community

class CommunityCreate(CreateView):
    model = Community
    success_url = reverse_lazy('server_list')
    fields = ['name','order']

class CommunityUpdate(UpdateView):
    model = Community
    success_url = reverse_lazy('server_list')
    fields = ['name', 'order']

class CommunityDelete(DeleteView):
    model = Community
    success_url = reverse_lazy('server_list')
