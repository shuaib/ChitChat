from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from chatroom.models import Message

from chatroom.forms import MessageForm

def index(request):
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			message = form.save()
	else:
		pass
	form = MessageForm()
	
	messages = Message.objects.all()
	if len(messages)>30:
		messages = messages[:30]
	return render_to_response("chatroom/index.html", {
		'form':form,
		'messages':messages,
		},
		context_instance=RequestContext(request)
		)
