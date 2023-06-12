from django.db import models
from django.contrib.auth.models import User
from item.models import Item

# Create your models here.
# model for conversations between clients and sellers
class Talk(models.Model):
    item = models.ForeignKey(Item, related_name='talks', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='talks')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-modified_at',)

class TalkMessage(models.Model):
    talk = models.ForeignKey(Talk, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

