from django.conf.urls import url

from .views import (
    PostView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
)

urlpatterns = [
    url(r'delete/(?P<pk>\d+)/$', PostDeleteView.as_view(),name='delete'),
    url(r'update/(?P<pk>\d+)/$', PostUpdateView.as_view(),name='update'),
    url(r'(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'create/$', PostCreateView.as_view(), name='create'),
    url(r'$', PostView.as_view(), name='template'),
]
