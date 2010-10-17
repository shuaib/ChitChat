from django.db import models

class Message(models.Model):
	message = models.CharField(max_length=240)
	timestamp = models.DateTimeField(auto_now=True)
	sender_name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.message

	class Meta:
		ordering = ['-id']
