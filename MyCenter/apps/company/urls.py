from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^$', views.company_list, name='company_list'),
    url(r'^(?P<c_id>\d+)$', views.company_detail, name='company')
]
