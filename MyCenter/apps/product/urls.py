from django.conf.urls import url
from product.views import CategoryView, cate_proView

urlpatterns = [
    url(r'^category/(?P<cate_id>\d+)/$', CategoryView.as_view(), name='CategoryView'),
    url(r'^category/$', cate_proView.as_view(), name='cate_pro')
]