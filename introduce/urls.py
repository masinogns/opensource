from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^story/', StoryView.as_view(), name='story'),
    url(r'^effect/', EffectView.as_view(), name='effect'),
    url(r'^future/', FutureView.as_view(), name='future'),
]
