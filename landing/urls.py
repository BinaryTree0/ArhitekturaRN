from django.conf.urls import url

from .views import (
    IndexView,
    AboutView,
    ContactView,
)

urlpatterns = [
    url(r'about$', AboutView.as_view(), name='about'),
    url(r'contact$', ContactView.as_view(), name='contact'),
    url(r'$', IndexView.as_view(), name='template'),
]
