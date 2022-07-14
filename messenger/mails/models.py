from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Mail(models.Model):
    from_user=models.CharField(max_length=100)
    to_user=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    body=models.TextField()
    time=models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('mails:mail_detail', kwargs={'id': self.id}) #reverse version of urlpattern
    
    def get_preview(self): #showing first 20 characters
        return self.body[:20]
