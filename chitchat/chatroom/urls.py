from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('chitchat.chatroom.views',
	url(r'^$', 'index', name='index'),
)
