from django.db import models

# Create your models here.
class ChatModel(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=255)
    msg=models.CharField(max_length=255)