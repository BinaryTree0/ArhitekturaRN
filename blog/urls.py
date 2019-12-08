from django.conf.urls import url

from .views import (
    BlogView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CommentDeleteView,
)

urlpatterns = [
    url(r'delete/comment/(?P<pk>\d+)/$', CommentDeleteView.as_view(),name='comment_delete'),
    url(r'update/(?P<pk>\d+)/$', BlogUpdateView.as_view(),name='update'),
    url(r'delete/(?P<pk>\d+)/$', BlogDeleteView.as_view(),name='delete'),
    url(r'(?P<pk>\d+)/$', BlogDetailView.as_view(), name='detail'),
    url(r'create/$', BlogCreateView.as_view(), name='create'),
    url(r'$', BlogView.as_view(), name='template'),
]
