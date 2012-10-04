from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user        = models.OneToOneField(User)
    birthday    = models.DateField()
    name        = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

# Create your models here.
#def create_user_account_callback(sender, instance, **kwargs):
#    useraccount, new = UserAccount.objects.get_or_create(user=instance)

#post_save.connect(create_user_account_callback, User)
