from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^$', views.company_list, name='company_list'),
    url(r'^(?P<c_id>\d+)$', views.company_detail, name='company'),
    url(r'^category$', views.company_type, name='company_type'),
    url(r'^search$', views.company_search, name='company_search')
]
