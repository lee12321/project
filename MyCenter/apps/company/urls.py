from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^(?P<c_id>\d+)$', views.company_detail, name='detail'),
    url(r'^category/$', views.company_type, name='company_type'),
    url(r'^search/', views.company_search, name='company_search'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^selfcheck/', views.self_check_list, name='self_check'),
]
