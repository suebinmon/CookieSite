from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Main, name='Main'),
	url(r'^intro/$', views.intro, name='intro'),
	url(r'^talk/$', views.index, name='index'),
	url(r'^QnA/$', views.QnA, name='qna'),
	url(r'^lock/$', views.lock, name='lock'),
	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^upload/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]
