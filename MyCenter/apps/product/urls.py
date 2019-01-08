from django.conf.urls import url

from product.views import CategoryView, cate_proView, CateSearchView

urlpatterns = [
    url(r'^category/', CategoryView.as_view(), name='CategoryView'),
    url(r'^search/', CateSearchView.as_view(), name='CateSearchView')
]