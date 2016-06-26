from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Opening(models.Model):
    request = models.TextField(max_length=2000)
    store = models.TextField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=250)
    desired_fee = models.PositiveSmallIntegerField(default=500)

    def __str__(self):
        return "{} wants {} from {} at {}".format(self.address,
                self.request, self.store, self.time)

class Bid(models.Model):
    opening = models.ForeignKey(
            'Opening',
            on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField() # Price in cents
    latitude = models.FloatField()
    longitude = models.FloatField()
