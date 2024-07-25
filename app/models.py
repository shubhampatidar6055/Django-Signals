from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.

class Usermodel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
@receiver(post_save,sender=Usermodel)
def mymodel_post_save(sender,instance,**kwargs):
    print("My model instence was save")

@receiver(pre_delete,sender=Usermodel)
def mymodel_post_delete(sender,instance,**kwargs):
    print("My model instence was Deleted")

