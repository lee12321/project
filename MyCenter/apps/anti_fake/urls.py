from django.conf.urls import url
from anti_fake.views import SdyproView, RealView, RealLookView, LookView

urlpatterns = [
    url(r'^sdypro/$', SdyproView.as_view(), name='sdypro'),
    url(r'^realdata/$', RealView.as_view(), name='realdata'),
    url(r'^real_look/$', RealLookView.as_view(), name='real_look'),
    url(r'^look/(?P<pro_id>\d+)/$', LookView.as_view(), name='look'),
]
