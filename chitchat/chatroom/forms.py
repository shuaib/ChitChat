from django import forms

from chatroom.models import Message

class MessageForm(forms.ModelForm):

	text = forms.CharField(max_length=240, required=True)
	
	class Meta:
		model = Message
		exclue = ('timestamp', 'sender')
