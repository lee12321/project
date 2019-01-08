from django.conf.urls import url
from product.views import CategoryView, DetailView

urlpatterns = [
    url(r'^category/(?P<cate_id>\d+)/$', CategoryView.as_view(), name='CategoryView'),
    url(r'^category/detail/(?P<pro_id>\d+)/$', DetailView.as_view(), name='DetailView'),
]
