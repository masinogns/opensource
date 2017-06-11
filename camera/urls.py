from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^situation/', SituationView.as_view(), name='situation'),
    url(r'^different/', DifferentView.as_view(), name='different'),
    url(r'^prevent/', PreventView.as_view(), name='prevent'),
]
