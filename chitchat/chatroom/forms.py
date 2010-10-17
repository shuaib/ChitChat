from django import forms

from chatroom.models import Message

class MessageForm(forms.ModelForm):

	message = forms.CharField(max_length=240, required=True)
	sender = forms.CharField(max_length=20, required=False)

	class Meta:
		model = Message
		exclue = ('timestamp')
