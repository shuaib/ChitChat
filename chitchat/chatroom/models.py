from django.db import models

class Message(models.Model):
	text = models.CharField(max_length=240)
	timestamp = models.DateTimeField(auto_now=True)
	sender = models.CharField(max_length=20, blank=True, null=True)

	def __unicode__(self):
		return self.message

	class Meta:
		ordering = ['-id']
