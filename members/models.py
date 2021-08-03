from django.db import models

class Member(models.Model):
    name         = models.CharField(max_length=200)
    email        = models.CharField(max_length=200)
    password     = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=200)
    address      = models.CharField(max_length=200, null=True)
    recommender  = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    coupon       = models.IntegerField(null=True)

    class Meta:
        db_table = 'members'