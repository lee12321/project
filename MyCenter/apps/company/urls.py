from django.conf.urls import url
from company.views import ContentView

urlpatterns = [
    url(r'^content/$', ContentView.as_view(), name='ContentView')
]