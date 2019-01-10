from django.conf.urls import url
from product.views import CategoryView, cate_proView, CateSearchView, DetailView

urlpatterns = [
    url(r'^category/', CategoryView.as_view(), name='CategoryView'),
    url(r'^search/', CateSearchView.as_view(), name='CateSearchView'),
    url(r'^(?P<pro_id>\d+)/$', DetailView.as_view(), name='DetailView'),
]
