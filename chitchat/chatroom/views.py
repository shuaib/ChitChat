from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from chatroom.forms import MessageForm

def index(request):
	if request.method == "POST":
		pass
	else:
		form = MessageForm()

	return render_to_response("chatroom/index.html", {
		'form':form,
		}
		context_request=RequestContext(request)
		)
