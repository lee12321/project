from django.conf.urls import url
from product.views import CategoryView

urlpatterns = [
    url(r'^category/(?P<cate_id>\d+)/$', CategoryView.as_view(), name='CategoryView')
]